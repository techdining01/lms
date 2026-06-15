from django import forms

from apps.academics.models import SchoolClass


class SchoolClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass

        fields = [
            "name",
            "department",
            "description",
        ]
