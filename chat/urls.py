from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^chatroom/$', views.chatroom, name='chatroom'),
    url(r'^proccess_msg/$', views.proccess_msg, name='proccess_msg'),
]
