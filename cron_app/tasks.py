import urllib.request
import json
from datetime import timedelta

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .models import RandomText
logger = get_task_logger(__name__)


@periodic_task(
    run_every=crontab(minute='*/1'),
    name="task_random_text",
    ignore_result=True
)
def task_random_text():
    with urllib.request.urlopen('https://baconipsum.com/api/?type=all-meat') as response:
        html = response.read()
    data = json.loads(html.decode('utf-8'))[0]
    text = RandomText(random_text=data)
    text.save()
    logger.info(data)
