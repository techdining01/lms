from django.db.models import Sum

from apps.exams.models import (
    Answer,
    ExamResult,
)
def generate_result(
    attempt,
):

    objective_score = (
        Answer.objects.filter(
            attempt=attempt,
            question__question_type__in=[
                "MCQ",
                "TRUE_FALSE",
                "FILL_BLANK",
            ],
        ).aggregate(total=Sum("marks_awarded"))["total"]
        or 0
    )

    subjective_score = (
        Answer.objects.filter(
            attempt=attempt,
            question__question_type__in=[
                "SHORT_ANSWER",
                "ESSAY",
            ],
        ).aggregate(total=Sum("marks_awarded"))["total"]
        or 0
    )

    total = objective_score + subjective_score

    percentage = (total / attempt.exam.total_marks) * 100

    return ExamResult.objects.update_or_create(
        attempt=attempt,
        defaults={
            "objective_score": objective_score,
            "subjective_score": subjective_score,
            "total_score": total,
            "percentage": percentage,
        },
    )