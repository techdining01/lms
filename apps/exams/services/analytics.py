from django.db.models import (
    Avg,
    Count,
)
def exam_statistics(
    exam,
):

    queryset = exam.examresult_set.all()

    return {
        "average": queryset.aggregate(avg=Avg("percentage"))["avg"],
        "attempts": queryset.count(),
    }