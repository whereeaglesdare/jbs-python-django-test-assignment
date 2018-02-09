from celery.decorators import task
from celery.utils.log import get_task_logger

from .httpbin import send_http_request


logger = get_task_logger(__name__)


@task(name="send_http_request_task")
def send_http_request_task(delay_sec):

    """sends an email when feedback form is filled successfully"""
    logger.info("Sent http request")
    return send_http_request(delay_sec)


