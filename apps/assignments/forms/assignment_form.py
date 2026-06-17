from django import forms

from apps.assignments.models.assignment import Assignment


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment

        fields = [
            "title",
            "instructions",
            "class_subject",
            "course",
            "due_date",
            "total_marks",
            "late_penalty_percentage",
            "allow_text_submission",
            "allow_file_submission",
            "max_attempts",
            "status",
            "published_at",
        ]

        widgets = {
            "instructions": forms.Textarea(attrs={"rows": 8}),
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
