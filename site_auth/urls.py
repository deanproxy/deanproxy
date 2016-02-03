from django.conf.urls import url
from site_auth import views

urlpatterns = (
	url(r'^$', views.index, name='auth_page_url'),
	url(r'^login/', views.login, name='auth_login_url'),
	url(r'^logout/', views.logout, name='auth_logout_url'),
	url(r'^password/$', views.password, name='auth_reset_password_url'),
	url(r'^password/reset/', views.reset_password, name='auth_reset_submit_url'),
)
