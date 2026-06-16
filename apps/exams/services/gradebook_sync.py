from apps.grades.models import Gradebook
def sync_exam_to_gradebook(
    result,
):

    attempt = result.attempt

    Gradebook.objects.update_or_create(
        student=attempt.student,
        class_subject=attempt.exam.class_subject,
        term=attempt.exam.term,
        defaults={"exam_score": result.total_score},
    )