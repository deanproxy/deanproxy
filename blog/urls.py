from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^posts/$', 'deanproxy.blog.views.index', name='blog_url'),
	url(r'^posts/\d+/\d+/(\d+)[-\w]+\.html', 'deanproxy.blog.views.show', name='blog_post_show_url'),
	url(r'^posts/tag/(\w+)', 'deanproxy.blog.views.show_by_tag', name='blog_tag_url'),
	url(r'^posts/new/', 'deanproxy.blog.views.new_post', name='blog_post_new_url'),
	url(r'^posts/create/', 'deanproxy.blog.views.create', name='blog_post_create_url'),
	url(r'^posts/edit/(\d+)', 'deanproxy.blog.views.edit', name='blog_post_edit_url'),
	url(r'^posts/update/(\d+)', 'deanproxy.blog.views.update', name='blog_post_update_url'),
	url(r'^posts/delete/(\d+)', 'deanproxy.blog.views.destroy', name='blog_post_delete_url'),
	url(r'^comments/create/', 'deanproxy.blog.views.create_comment', name='blog_comment_create_url'),
#	url(r'^comments/update/(\d+)', 'deanproxy.blog.views.update_comment'),
	url(r'^comments/delete/(\d+)', 'deanproxy.blog.views.delete_comment', name='blog_comment_delete_url'),
	url(r'^posts/search/', 'deanproxy.blog.views.search', name='blog_search_url'),
)