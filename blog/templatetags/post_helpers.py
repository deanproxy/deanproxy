from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def total_comments(total):
	string = "Comment"
	if (total != 1):
		string += 's'
	return "%d %s" % (total, string)

@register.simple_tag
def tags_to_string(tags):
	html = ''
	total_tags = len(tags)
	for i, tag in enumerate(tags):
		html += """<a href="/blog/posts/tag/{0}">{0}</a>""".format(tag.name)
		if i+1 < total_tags:
			html += ', '
	return html


@register.inclusion_tag('blog/_latest_posts.html')
def latest_posts():
	posts = Post.objects.order_by('created_at')[:5]
	return {'posts':posts}