from apps.report_cards.models import ReportCard


def calculate_positions(
    term,
):

    cards = ReportCard.objects.filter(term=term).order_by("-average_score")

    for position, card in enumerate(
        cards,
        start=1,
    ):
        card.position = position
        card.save(update_fields=["position"])
