from celery import shared_task

from apps.communication.models import Notification



@shared_task
def send_notification(
    notification_id,
):
    pass