from django import template
import re
from blog.models import Post

register = template.Library()

@register.simple_tag
def css(file):
	return '<link rel="stylesheet" type="text/css" href="/static/css/%s"/>' % file

@register.simple_tag
def js(file):
	return '<script src="/static/js/%s"></script>' % file

@register.simple_tag
def img(file):
	return '<img src="/static/images/%s"/>' % file

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
	return location

@register.simple_tag
def existing_post_actions(uri):
	html = ''
	match = re.match('/blog/posts/\d+/\d+/(\d+)[-\w]+\.html', uri)
	if match:
		id = match.groups()[0]
		html = """
			<li><a href="/blog/posts/edit/{0}">Edit This Post</a></li>
		""".format(id)
	return html


