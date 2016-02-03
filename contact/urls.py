from django.conf.urls import url
from contact import views

urlpatterns = (
	url(r'^$', views.index, name='contact_url'),
	url(r'^send/', views.send, name='contact_send_url'),
)
