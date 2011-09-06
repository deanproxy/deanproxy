from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'contact.views.index', name='contact_url'),
	url(r'^send/', 'contact.views.send', name='contact_send_url'),
)