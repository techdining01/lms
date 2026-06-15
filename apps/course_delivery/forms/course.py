from django import forms

from apps.course_delivery.models.course import AcademicCourse


class CourseForm(forms.ModelForm):
    class Meta:
        model = AcademicCourse

        fields = [
            "title",
            "description",
            "is_published",
        ]
