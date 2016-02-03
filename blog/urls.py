from django.conf.urls import url
from blog import views

urlpatterns = ( 
	url(r'^posts/$', views.index, name='blog_url'),
	url(r'^posts/\d+/\d+/(\d+)[-\w]+\.html', views.show, name='blog_post_show_url'),
	url(r'^posts/tag/(\w+)', views.show_by_tag, name='blog_tag_url'),
	url(r'^posts/new/', views.new_post, name='blog_post_new_url'),
	url(r'^posts/create/', views.create, name='blog_post_create_url'),
	url(r'^posts/edit/(\d+)', views.edit, name='blog_post_edit_url'),
	url(r'^posts/update/(\d+)', views.update, name='blog_post_update_url'),
	url(r'^posts/delete/(\d+)', views.destroy, name='blog_post_delete_url'),
	url(r'^comments/create/', views.create_comment, name='blog_comment_create_url'),
#	url(r'^comments/update/(\d+)', views.update_comment),
	url(r'^comments/delete/(\d+)', views.delete_comment, name='blog_comment_delete_url'),
	url(r'^posts/search/', views.search, name='blog_search_url'),
)
