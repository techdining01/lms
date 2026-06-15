from django import forms

from apps.assignments.models import assignment_submission


class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = assignment_submission

        fields = [
            "text_answer",
        ]

        widgets = {
            "text_answer": forms.Textarea(
                attrs={
                    "rows": 8,
                }
            )
        }

