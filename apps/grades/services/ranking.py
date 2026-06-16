from django.db.models import F

from apps.report_cards.models import ReportCard

def calculate_class_positions(
    school_class,
    term,
):

    cards = ReportCard.objects.filter(
        school_class=school_class,
        term=term,
    ).order_by("-average")

    total_students = cards.count()

    current_position = 1

    for card in cards:
        card.position = current_position

        card.class_size = total_students

        card.save(
            update_fields=[
                "position",
                "class_size",
            ]
        )

        current_position += 1