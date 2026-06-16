from django.views.generic import UpdateView

from apps.exams.models import Answer
class SubjectiveMarkingView(UpdateView):
    model = Answer

    fields = ["marks_awarded"]

    template_name = "exams/grading/mark.html"