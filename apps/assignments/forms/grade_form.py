from django import forms

from apps.assignments.models import AssignmentGrade


class GradeForm(forms.ModelForm):
    class Meta:
        model = AssignmentGrade

        fields = [
            "raw_score",
            "feedback",
        ]
