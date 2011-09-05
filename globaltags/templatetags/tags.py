from django import template
import re

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
	match = re.match('/(\w+)/', uri)
	if match and match.groups()[0] != 'blog':
		location = match.groups()[0]
	return location

@register.simple_tag
def existing_post_actions(uri):
	html = ''
	print uri
	match = re.match('/blog/posts/\d+/\d+/(\d+)[-\w]+\.html', uri)
	if match:
		id = match.groups()[0]
		html = """
			<li><a href="/blog/posts/edit/{0}">Edit This Post</a></li>
		""".format(id)
	return html


# TODO: Store results in DB. Make model do the work there, tag should only call a method on the model.




