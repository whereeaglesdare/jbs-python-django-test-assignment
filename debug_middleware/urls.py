from django.conf.urls import url
from .views import custom_middleware_view

urlpatterns = [
    url(r'^request_handler/$', custom_middleware_view, name='middleware_list'),
]