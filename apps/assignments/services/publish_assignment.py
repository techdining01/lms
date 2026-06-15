from django.utils import timezone


def publish_assignment(assignment):
    assignment.status = assignment.Status.PUBLISHED

    assignment.published_at = timezone.now()

    assignment.save()

    return assignment
