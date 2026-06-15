from django.utils import timezone


def is_late_submission(
    assignment,
):

    return timezone.now() > assignment.due_date


def calculate_penalty(
    assignment,
    score,
):

    if not is_late_submission(assignment):
        return score

    deduction = (score * assignment.late_penalty_percentage) / 100

    return score - deduction
