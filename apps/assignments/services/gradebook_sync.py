from django.db.models import Avg

from apps.assignments.models import AssignmentGrade

from apps.grades.models import AssessmentScore


def sync_assignment_score(
    student,
    class_subject,
    term,
):

    average = (
        AssignmentGrade.objects.filter(
            submission__student=student,
            submission__assignment__class_subject=class_subject,
        ).aggregate(avg=Avg("final_score"))["avg"]
        or 0
    )

    AssessmentScore.objects.update_or_create(
        student=student,
        class_subject=class_subject,
        term=term,
        defaults={"assignment_score": average},
    )