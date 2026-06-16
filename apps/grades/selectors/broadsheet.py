from apps.report_cards.models import ReportCard


def get_broadsheet(
    school_class,
    term,
):

    return (
        ReportCard.objects.filter(
            school_class=school_class,
            term=term,
        )
        .prefetch_related("subjects")
        .order_by("position")
    )