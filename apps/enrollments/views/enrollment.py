from django.views.generic import (
    ListView,
    CreateView,
)

from django.urls import reverse_lazy

from apps.enrollments.models.enrollment import StudentEnrollment

from apps.enrollments.forms.enrollment import EnrollmentForm


class EnrollmentListView(ListView):
    model = StudentEnrollment

    template_name = "enrollment/list.html"

    context_object_name = "enrollments"


class EnrollmentCreateView(CreateView):
    model = StudentEnrollment

    form_class = EnrollmentForm

    template_name = "enrollment/create.html"

    success_url = reverse_lazy("enrollment:list")
