from apps.exams.models import ExamAttempt


def get_or_resume_attempt(
    exam,
    student,
):

    return ExamAttempt.objects.filter(
        exam=exam,
        student=student,
        status="IN_PROGRESS",
    ).first()


