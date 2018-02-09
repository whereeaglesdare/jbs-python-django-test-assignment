from django.db import models
from db_logger.models import DBLoggerModel
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

class MiddlewareModel(models.Model):
    request_method = models.CharField(max_length=10)
    request_path = models.TextField()
    dt_request = models.DateTimeField(auto_now=True)




@receiver(post_save, sender=MiddlewareModel)
def save_signal(sender, instance, **kwargs):
    log = DBLoggerModel(model=instance._meta.db_table, method='create')
    log.save()
    # DBLoggerModel.objects.all().delete()


@receiver(post_delete, sender=MiddlewareModel)
def delete_signal(sender, instance, **kwargs):
    log = DBLoggerModel(model=instance._meta.db_table, method='delete')
    log.save()