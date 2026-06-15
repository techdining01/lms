from django.forms import inlineformset_factory

from apps.assignments.models import (
    SubmissionAttachment,
    assignment_submission,
)


SubmissionAttachmentFormSet = inlineformset_factory(
    assignment_submission,
    SubmissionAttachment,
    fields=["file"],
    extra=3,
    can_delete=True,
)
