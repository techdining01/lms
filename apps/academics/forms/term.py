from django import forms

from apps.academics.models import Term


class TermForm(forms.ModelForm):
    class Meta:
        model = Term

        fields = [
            "session",
            "name",
            "start_date",
            "end_date",
            "is_current",
        ]
