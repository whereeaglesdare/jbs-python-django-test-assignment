from django.shortcuts import render
from .models import DBLoggerModel


def db_logger_view(request):
    db_logs = DBLoggerModel.objects.all().values('model', 'method').order_by('-id')[:10]
    return render(request, 'db_logger/db_logger.html', {'logs': db_logs})
