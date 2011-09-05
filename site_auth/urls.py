from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'deanproxy.site_auth.views.index', name='auth_page_url'),
	url(r'^login/', 'deanproxy.site_auth.views.login', name='auth_login_url'),
	url(r'^logout/', 'deanproxy.site_auth.views.logout', name='auth_logout_url'),
	url(r'^password/$', 'site_auth.views.password', name='auth_reset_password_url'),
	url(r'^password/reset/', 'site_auth.views.reset_password', name='auth_reset_submit_url'),
)