from django.db.models import (
    Count,
    Avg,
)

from apps.assignments.models.assignment_submission import (
    AssignmentGrade,
    AssignmentSubmission,
)


def assignment_analytics():

    return {
        "submissions": AssignmentSubmission.objects.count(),
        "average_score": AssignmentGrade.objects.aggregate(avg=Avg("final_score"))[
            "avg"
        ],
    }