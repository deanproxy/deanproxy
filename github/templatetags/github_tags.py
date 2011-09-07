from django import template
from github.models import Commit
from django.utils import simplejson
from dateutil.parser import parse
import urllib2
import datetime
import logging

register = template.Library()

@register.simple_tag
def last_commit(project_name):
	html = '<span class="error">Error getting last github commit</span>'
	commit = get_commit(project_name)
	if commit:
		html = """
				<div class="githubCommit">
		  			Last commit: <span class="message">%s</span>
		  			<span class="author">by %s</span>
		  			<time datetime="%s">on %s</time>
	    		</div>
	    """ % (commit.message, commit.committer, commit.committed_date, commit.committed_date.strftime("%d %b, %Y"))

	return html


def get_latest_commit(project_name):
	json = None
	try:
		url = urllib2.urlopen('http://github.com/api/v2/json/commits/list/deanproxy/%s/master' % project_name)
		data = url.read()
		json = simplejson.loads(data)
	except ValueError:
		logging.error('There was a problem parsing JSON data: %s' % json)
	except urllib2.URLError, error:
		logging.error('A URLError exception was raised: %s ' % error)
	except urllib2.HTTPError, error:
		logging.error('An HTTPError was raised: %s' % error)

	if not json:
		return None
	return json['commits'][0]

def get_commit(project_name):
	now = datetime.datetime.now()
	future = datetime.timedelta(0, 300) # 5 Minutes
	try:
		commit = Commit.objects.get(pk=project_name)
	except Commit.DoesNotExist:
		commit = None

	if not commit or now - commit.updated_at >= future:
		if commit:
			commit.delete()
		json = get_latest_commit(project_name)
		if json:
			date = parse(json['committed_date'])
			commit = Commit.objects.create(
				committed_date=date,
				message=json['message'],
				committer=json['committer']['name'],
				project=project_name
			)
			commit.save()

	return commit
