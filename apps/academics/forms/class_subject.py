from django import forms

from apps.academics.models import ClassSubject


class ClassSubjectForm(forms.ModelForm):
    class Meta:
        model = ClassSubject

        fields = [
            "school_class",
            "subject",
            "teacher",
        ]
