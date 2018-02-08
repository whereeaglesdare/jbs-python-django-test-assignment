from django import template
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
register = template.Library()

@register.simple_tag()
def edit_link(model_object):
    try:
        content_type = ContentType.objects.get_for_model(model_object)
    except AttributeError:
        return '/admin'
    return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(model_object.id,))
