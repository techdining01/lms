from django.views.generic import CreateView

from django.urls import reverse_lazy

from apps.assignments.models import assignment_submission

from apps.assignments.forms.submission_form import AssignmentSubmissionForm


class SubmitAssignmentView(CreateView):
    model = assignment_submission

    form_class = AssignmentSubmissionForm

    template_name = "assignments/submit.html"

    def form_valid(
        self,
        form,
    ):
        form.instance.student = self.request.user

        form.instance.assignment_id = self.kwargs["pk"]

        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy("assignments:list")
