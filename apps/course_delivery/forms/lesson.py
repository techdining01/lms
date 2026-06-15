from django import forms

from apps.course_delivery.models.lesson import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson

        fields = [
            "title",
            "lesson_type",
            "content",
            "order",
        ]
