from apps.communication.tasks.send_email import send_assignment_email


def notify_assignment_published(assignment):

    send_assignment_email.delay(assignment.id)
