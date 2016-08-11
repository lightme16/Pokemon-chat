from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^get_messages/$', views.get_messages, name='get_messages'),
    url(r'^process_msg/$', views.process_msg, name='process_msg'),
    url(r'^get_messagesJSON/$', views.get_messagesJSON, name='get_messagesJSON'),

]
