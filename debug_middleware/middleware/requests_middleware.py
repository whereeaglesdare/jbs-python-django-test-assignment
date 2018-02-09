from ..models import MiddlewareModel
from django.utils.deprecation import MiddlewareMixin


class CustomDebugMiddleware(MiddlewareMixin):
    def process_request(self, request):
            new_http_information = MiddlewareModel(request_method=request.method, request_path=request.get_full_path())
            new_http_information.save()

