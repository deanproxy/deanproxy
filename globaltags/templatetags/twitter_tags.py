from django import template
from dateutil.parser import parse
from django.core.cache import cache
import urllib2
import logging
import json

register = template.Library()

@register.inclusion_tag('base/_twitter.html')
def twitter(username):
	tweets = cache.get('twitter')
	if not tweets:
		tweets = []
		try:
			url = urllib2.urlopen('https://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&count=3&include_entities=true' % username)
			data = url.read()
			json = json.loads(data)
		except ValueError:
			logging.error('There was a problem parsing JSON data: %s' % json)
		except urllib2.URLError, error:
			logging.error('A URLError exception was raised: %s ' % error)
		except urllib2.HTTPError, error:
			logging.error('An HTTPError was raised: %s' % error)
		else:
			# I only need the text and the created at portions, and only 5 of them
			for item in json[:5]:
				tweets.append({
					'created_at': parse(item['created_at']),
					'text': item['text']
				})
			cache.set('twitter', tweets, 300)

	return {'tweets' : tweets}
