from apps.communication.models import Notification


def create_notification(
    *,
    recipient,
    title,
    message,
    channel,
):

    return Notification.objects.create(
        recipient=recipient,
        title=title,
        message=message,
        channel=channel,
    )
