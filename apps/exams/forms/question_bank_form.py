from django import forms

from apps.exams.models import QuestionBank


class QuestionBankForm(forms.ModelForm):
    class Meta:
        model = QuestionBank

        fields = [
            "subject",
            "course",
            "question_text",
            "question_type",
            "difficulty",
            "marks",
            "explanation",
        ]

