from django.db import models


class MiddlewareModel(models.Model):
    request_method = models.CharField(max_length=10)
    request_path = models.TextField()
    dt_request = models.DateTimeField(auto_now=True)

