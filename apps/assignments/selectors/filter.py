from apps.assignments.models import Assignment


def filter_assignments(
    status=None,
):

    qs = Assignment.objects.all()

    if status:
        qs = qs.filter(status=status)

    return qs
