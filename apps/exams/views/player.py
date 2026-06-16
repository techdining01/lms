from django.shortcuts import (
    get_object_or_404, render,
    redirect,
)

from django.contrib.auth.decorators import (
    login_required,
)

from apps.exams.models import (
    Exam,
    ExamAttempt,
)


@login_required
def start_exam(
    request,
    exam_id,
):

    exam = get_object_or_404(
        Exam,
        pk=exam_id,
    )

    attempt, created = ExamAttempt.objects.get_or_create(
        exam=exam,
        student=request.user,
        status=ExamAttempt.Status.IN_PROGRESS,
    )

    return redirect(
        "exams:player",
        attempt.id,
    )


@login_required
def exam_player(
    request,
    attempt_id,
):

    attempt = ExamAttempt.objects.select_related("exam").get(pk=attempt_id)

    questions = attempt.exam.exam_questions.select_related("question").prefetch_related(
        "question__options"
    )

    return render(
        request,
        "exams/player.html",
        {
            "attempt": attempt,
            "questions": questions,
        },
    )


