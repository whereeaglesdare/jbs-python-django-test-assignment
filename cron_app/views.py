from django.shortcuts import render
from .models import RandomText


def random_text_view(request):
    text = RandomText.objects.all().last().random_text
    return render(request, 'cron_app/cron.html', {"text": text})
