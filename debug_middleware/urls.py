from django.conf.urls import url
from .views import custom_middleware_view, settings_context_view

urlpatterns = [
    url(r'^request_handler/$', custom_middleware_view, name='middleware_list'),
    url(r'^settings-context-processor/$', settings_context_view, name='settings_context_view'),
]