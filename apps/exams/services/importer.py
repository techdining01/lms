import pandas as pd

from apps.exams.models.question_bank import QuestionBank
from apps.exams.models.question_bank_option import QuestionBankOption

def import_questions_from_excel(
    file,
    subject,
    created_by,
):
    df = pd.read_excel(file)

    for row in df.itertuples():
        question = QuestionBank.objects.create(
            subject=subject,
            question_text=row.question,
            question_type="MCQ",
            created_by=created_by,
        )

        QuestionBankOption.objects.create(
            question=question,
            option_text=row.option_a,
            is_correct=row.correct == "A",
        )

        QuestionBankOption.objects.create(
            question=question,
            option_text=row.option_b,
            is_correct=row.correct == "B",
        )

        QuestionBankOption.objects.create(
            question=question,
            option_text=row.option_c,
            is_correct=row.correct == "C",
        )

        QuestionBankOption.objects.create(
            question=question,
            option_text=row.option_d,
            is_correct=row.correct == "D",
        )





