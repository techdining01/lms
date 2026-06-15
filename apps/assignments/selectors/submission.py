from apps.assignments.models import assignment_submission


def get_student_submissions(student):
    return assignment_submission.objects.filter(student=student).select_related(
        "assignment"
    )


