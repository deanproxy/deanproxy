import datetime
from django import template
from twitter.models import Tweet, Twitter
from django.utils import simplejson
import urllib2
import logging
import time

register = template.Library()

@register.inclusion_tag('../templates/_twitter.html')
def twitter(username):
	tweets = Tweet.objects.all()
	twitter = Twitter.objects.all()
	future = datetime.timedelta(0, 120)

	if not twitter:
		twitter = Twitter.objects.create()
		last_updated = datetime.timedelta(0, 0)
	else:
		twitter = twitter[0]
		last_updated = twitter.last_updated

	if last_updated <= last_updated + future:
		twitter.last_updated += future
		twitter.save()
		tweets.delete()
		try:
			url = urllib2.urlopen('http://twitter.com/statuses/user_timeline.json?screen_name=%s&include_rts=true&trim_user=true' % username)
			data = url.read()
			json = simplejson.loads(data)
		except ValueError:
			logging.error('There was a problem parsing JSON data: %s' % json)
		except urllib2.URLError, error:
			logging.error('A URLError exception was raised: %s ' % error)
		except urllib2.HTTPError, error:
			logging.error('An HTTPError was raised: %s' % error)
		else:
			# I only need the text and the created at portions, and only 5 of them
			for item in json[:5]:
				date = time.strptime(item['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
				Tweet.objects.create(text=item['text'], created_at=time.strftime('%Y-%m-%d', date))
			tweets = Tweet.objects.all()

	return {'tweets' : tweets}