from django.db.models import Avg

from apps.grades.models import Gradebook

from apps.report_cards.models import ReportCard


def generate_report_card(
    *,
    student,
    term,
):

    average = (
        Gradebook.objects.filter(
            student=student,
            term=term,
        ).aggregate(avg=Avg("total_score"))["avg"]
        or 0
    )

    return ReportCard.objects.create(
        student=student,
        term=term,
        average_score=average,
    )
