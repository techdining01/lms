from apps.exams.models import Answer


def save_answer(
    *,
    attempt,
    question,
    answer_text=None,
    selected_option=None,
):

    Answer.objects.update_or_create(
        attempt=attempt,
        question=question,
        defaults={
            "text_answer": answer_text or "",
            "selected_option": selected_option,
        },
    )