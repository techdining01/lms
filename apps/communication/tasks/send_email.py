from celery import shared_task


@shared_task
def send_assignment_email(
    assignment_id,
):
    pass
