from apps.assignments.models import Assignment


def get_published_assignments():

    return (
        Assignment.objects.filter(status=Assignment.Status.PUBLISHED)
        .select_related("created_by")
        .prefetch_related("attachments")
    )
