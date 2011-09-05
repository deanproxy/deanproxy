from django.conf.urls.defaults import patterns, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'deanproxy.blog.views.index'),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # url(r'^deanproxy/', include('deanproxy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^blog/posts/$', 'deanproxy.blog.views.index'),
	url(r'^blog/posts/\d+/\d+/(\d+)[-\w]+\.html', 'deanproxy.blog.views.show'),
	url(r'^blog/posts/tag/(\w+)', 'deanproxy.blog.views.show_by_tag'),
	url(r'^blog/posts/new/', 'deanproxy.blog.views.new_post'),
	url(r'^blog/posts/create/', 'deanproxy.blog.views.create'),
	url(r'^blog/posts/edit/(\d+)', 'deanproxy.blog.views.edit'),
	url(r'^blog/posts/update/(\d+)', 'deanproxy.blog.views.update'),
	url(r'^blog/posts/delete/(\d+)', 'deanproxy.blog.views.destroy'),
	url(r'^blog/comments/create/', 'deanproxy.blog.views.create_comment'),
#	url(r'^blog/comments/update/(\d+)', 'deanproxy.blog.views.update_comment'),
	url(r'^blog/comments/delete/(\d+)', 'deanproxy.blog.views.delete_comment'),
	url(r'^blog/posts/search/', 'deanproxy.blog.views.search'),

#	url(r'^code/$', 'deanproxy.blog.views.code'),
#	url(r'^about/$', 'deanproxy.blog.views.about'),
#	url(r'^music/$', 'deanproxy.blog.views.music'),

	url(r'^admin/$', 'deanproxy.site_auth.views.index'),
	url(r'^admin/login/', 'deanproxy.site_auth.views.login'),
	url(r'^admin/logout/', 'deanproxy.site_auth.views.logout'),

#	url(r'^contact/$', 'deanproxy.contact.views.index'),
#	url(r'^contact/send/', 'deanproxy.contact.views.send'),
)
