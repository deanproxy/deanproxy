from django import template

register = template.Library()

@register.inclusion_tag('base/_github.html')
def last_commit(commit):
	return {'commit':commit}