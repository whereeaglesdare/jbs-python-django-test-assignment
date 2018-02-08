from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='user_info'),
    url(r'^login/$', auth_views.login, {'template_name': 'user_profile/login.html'}, name='login'),
    url(r'^edit_profile/$', views.edit_user, name='account_update'),
]