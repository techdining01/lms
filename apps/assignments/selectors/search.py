from django.db.models import Q

from apps.assignments.models import Assignment


def search_assignments(
    query,
):

    return Assignment.objects.filter(
        Q(title__icontains=query) | Q(instructions__icontains=query)
    )
