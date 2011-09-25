from django import template
from django.utils import simplejson
from dateutil.parser import parse
from django.core.cache import cache
import urllib2
import logging
from django.utils.html import escape

register = template.Library()

def get_latest_commit(project_name):
	commit = {}
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

	if json:
		most_recent = json['commits'][0]
		commit['committed_date'] = parse(most_recent['committed_date'])
		commit['message'] = most_recent['message']
		commit['committer'] = most_recent['committer']['name']

	return commit

@register.simple_tag
def last_commit(project_name):
	cached_key = 'git-' + project_name
	html = '<span class="error">Error getting last github commit</span>'
	commit = cache.get(cached_key)
	if not commit:
		commit = get_latest_commit(project_name)

	if commit:
		cache.set(cached_key, commit, 300)
		html = """
				<div class="githubCommit">
		  			Last commit: <span class="message">%s</span>
		  			<span class="author">by %s</span>
		  			<time datetime="%s">on %s</time>
	    		</div>
	    """ % (escape(commit['message']), escape(commit['committer']), commit['committed_date'],
			   commit['committed_date'].strftime("%d %b, %Y"))

	return html
