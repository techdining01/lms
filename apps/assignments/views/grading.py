from django.views.generic import UpdateView

from apps.assignments.models import AssignmentGrade

from apps.assignments.forms.grade_form import GradeForm


class GradeSubmissionView(UpdateView):
    model = AssignmentGrade

    form_class = GradeForm

    template_name = "assignments/grading/detail.html"
