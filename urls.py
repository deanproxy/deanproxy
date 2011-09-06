from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index'),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # url(r'^deanproxy/', include('deanproxy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include('site_auth.urls')),
	url(r'^contact/', include('contact.urls')),

#	url(r'^code/$', 'blog.views.code', name='code_view_url'),
#	url(r'^about/$', 'blog.views.about', name='about_view_url'),
#	url(r'^music/$', 'blog.views.music', name='music_view_url'),
#

)
