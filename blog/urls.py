from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^posts/$', 'blog.views.index', name='blog_url'),
	url(r'^posts/\d+/\d+/(\d+)[-\w]+\.html', 'blog.views.show', name='blog_post_show_url'),
	url(r'^posts/tag/(\w+)', 'blog.views.show_by_tag', name='blog_tag_url'),
	url(r'^posts/new/', 'blog.views.new_post', name='blog_post_new_url'),
	url(r'^posts/create/', 'blog.views.create', name='blog_post_create_url'),
	url(r'^posts/edit/(\d+)', 'blog.views.edit', name='blog_post_edit_url'),
	url(r'^posts/update/(\d+)', 'blog.views.update', name='blog_post_update_url'),
	url(r'^posts/delete/(\d+)', 'blog.views.destroy', name='blog_post_delete_url'),
	url(r'^comments/create/', 'blog.views.create_comment', name='blog_comment_create_url'),
#	url(r'^comments/update/(\d+)', 'blog.views.update_comment'),
	url(r'^comments/delete/(\d+)', 'blog.views.delete_comment', name='blog_comment_delete_url'),
	url(r'^posts/search/', 'blog.views.search', name='blog_search_url'),
)
