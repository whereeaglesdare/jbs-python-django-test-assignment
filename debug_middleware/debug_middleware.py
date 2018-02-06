from yourapp.models import MiddlewareModel


class CustomDebugMiddleware_first(object):
    def process_request(self, request):
            print(request)
            # new_http_information = MiddlewareModelfo=INFO_YOU_WANT_TO_SAVE)
            # new_http_information.save()