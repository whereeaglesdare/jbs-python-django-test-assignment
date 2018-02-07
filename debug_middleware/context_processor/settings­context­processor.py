# from django.template.context_processors import request
from django.conf import settings
# from django.template import RequestContext


def show_settings(request):
    return {'settings' :settings.__dict__['_wrapped'].__dict__}
