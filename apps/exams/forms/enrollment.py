from django import forms

from apps.enrollments.models.enrollment import StudentEnrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = StudentEnrollment

        fields = [
            "student",
            "session",
            "school_class",
        ]
