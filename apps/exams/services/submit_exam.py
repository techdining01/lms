from django.utils import timezone


def submit_exam(
    attempt,
):

    attempt.status = attempt.Status.SUBMITTED

    attempt.submitted_at = timezone.now()

    attempt.save()

    return attempt
