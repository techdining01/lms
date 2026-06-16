from apps.exams.models import ExamResult


def calculate_exam_positions(
    exam,
):

    results = (
        ExamResult.objects
        .filter(
            attempt__exam=exam
        )
        .order_by(
            "-percentage"
        )
    )

    for index, result in enumerate(
        results,
        start=1,
    ):
        result.position = index

        result.save(
            update_fields=[
                "position"
            ]
        )