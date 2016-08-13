from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^save_new_msg/$', views.save_new_msg, name='save_new_msg'),
    url(r'^get_new_messages/$', views.get_new_messages, name='get_new_messages'),
    url(r'^reset/$', views.reset, name='reset'),

]
