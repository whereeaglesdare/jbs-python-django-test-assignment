from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import DBLoggerModel

IGNORE_INSTANCES  = ('MiddlewareModel', 'DBLoggerModel')

@receiver(post_save)
def callback_updated_created(sender, instance, created, **kwargs):
    if instance.__class__.__name__ in IGNORE_INSTANCES:
        return
    elif created:
        log = DBLoggerModel(model=instance._meta.db_table, method='update')
        log.save()
    else:
        log = DBLoggerModel(model=instance._meta.db_table, method='update')
        log.save()

@receiver(post_delete)
def callback_delete(sender, instance, **kwargs):
    log = DBLoggerModel(model=instance._meta.db_table, method='delete')
    log.save()