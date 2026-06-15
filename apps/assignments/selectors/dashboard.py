from django.db.models import Count

from apps.assignments.models import (
    Assignment,
    assignment_submission,
)


def assignment_dashboard():

    return {
        "total_assignments": Assignment.objects.count(),
        "total_submissions": assignment_submission.objects.count(),
        "published_assignments": Assignment.objects.filter(status="PUBLISHED").count(),
    }
