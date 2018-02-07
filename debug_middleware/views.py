from django.shortcuts import render
from .models import MiddlewareModel


def custom_middleware_view(request):
    stored_requests = MiddlewareModel.objects.all().values()[:10]
    return render(request, 'debug_middleware/handler.html',  {'stored_requests': stored_requests})


def settings_context_view(request):
    return render(request, 'template_context_processor/template_context_processor.html')