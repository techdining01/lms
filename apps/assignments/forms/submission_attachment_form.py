from django import forms

from apps.assignments.models import SubmissionAttachment


class SubmissionAttachmentForm(forms.ModelForm):
    class Meta:
        model = SubmissionAttachment

        fields = ["file"]
