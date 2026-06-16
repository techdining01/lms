from decimal import Decimal

from apps.exams.models import (
    Answer,
)


def autograde_attempt(
    attempt,
):
    total_score = Decimal("0")

    answers = Answer.objects.select_related(
        "question",
        "selected_option",
    ).filter(attempt=attempt)

    for answer in answers:
        question = answer.question

        if question.question_type not in [
            "MCQ",
            "TRUE_FALSE",
            "FILL_BLANK",
        ]:
            continue

        if answer.selected_option and answer.selected_option.is_correct:
            answer.is_correct = True

            answer.marks_awarded = question.marks

            total_score += question.marks

            answer.save(
                update_fields=[
                    "is_correct",
                    "marks_awarded",
                ]
            )

    return total_score

