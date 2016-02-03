from django import template
from django.utils.safestring import mark_safe
import re
from blog.models import Post

register = template.Library()

@register.simple_tag
def css(file):
	return mark_safe('<link rel="stylesheet" type="text/css" href="/static/css/%s"/>' % file)

@register.simple_tag
def js(file):
	return mark_safe('<script src="/static/js/%s"></script>' % file)

@register.simple_tag
def img(file):
	return mark_safe('<img src="/static/images/%s"/>' % file)

@register.simple_tag
def title(uri):
	location = 'home'
	match = re.match('/(\w+)/(?:\w+/\d+/\d+/(\d+)[-\w]+\.html)?', uri)
	if match:
		loc,id = match.groups()
		if loc == 'blog':
			# We want the location to be 'home' if there is no post shown,
			# Or the post's title if we are showing a post.
			if id:
				post = Post.objects.get(pk=int(id))
				location = post.title
		else:
			location = loc
	return mark_safe(location)

@register.simple_tag
def existing_post_actions(uri):
	html = ''
	match = re.match('/blog/posts/\d+/\d+/(\d+)[-\w]+\.html', uri)
	if match:
		id = match.groups()[0]
		html = """
			<li><a href="/blog/posts/edit/{0}">Edit This Post</a></li>
		""".format(id)
	return mark_safe(html)


