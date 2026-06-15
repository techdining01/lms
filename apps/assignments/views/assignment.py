from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)

from django.urls import reverse_lazy

from apps.assignments.models import Assignment

from apps.assignments.forms.assignment_form import AssignmentForm


class AssignmentListView(ListView):
    model = Assignment

    paginate_by = 20

    template_name = "assignments/list.html"

    context_object_name = "assignments"


class AssignmentCreateView(CreateView):
    model = Assignment

    form_class = AssignmentForm

    template_name = "assignments/create.html"

    success_url = reverse_lazy("assignments:list")

    def form_valid(
        self,
        form,
    ):
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class AssignmentDetailView(DetailView):
    model = Assignment

    template_name = "assignments/detail.html"
