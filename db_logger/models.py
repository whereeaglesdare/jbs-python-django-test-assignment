from django.db import models

# Create your models here.


class DBLoggerModel(models.Model):
    method_choices = (
        (1, 'update'),
        (2, 'create'),
        (3, 'delete'),
    )
    model = models.CharField(max_length=100)
    method = models.CharField(max_length=10, choices=method_choices)