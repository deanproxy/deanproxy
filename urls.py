from django.conf.urls import url, include
from django.conf import settings
from base import views as base_views
from blog import urls as bu
from blog import views as blog_views
from site_auth import urls as sa
from contact import urls as cu
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = (
    # Examples:
    url(r'^$', blog_views.index),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    # url(r'^deanproxy/', include('deanproxy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^blog/', include(bu)),
	url(r'^admin/', include(sa)),
	url(r'^contact/', include(cu)),

	url(r'^code/$', base_views.code, name='code_url'),
	url(r'^about/$', base_views.about, name='about_url'),
	url(r'^music/$', base_views.music, name='music_url'),

)
