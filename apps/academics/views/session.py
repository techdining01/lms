from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

from django.urls import reverse_lazy

from apps.academics.models import AcademicSession
from apps.academics.forms.session import AcademicSessionForm


class SessionListView(ListView):
    model = AcademicSession

    template_name = "academics/session/list.html"

    context_object_name = "sessions"


class SessionCreateView(CreateView):
    model = AcademicSession

    form_class = AcademicSessionForm

    template_name = "academics/session/create.html"

    success_url = reverse_lazy("academics:session-list")


class SessionUpdateView(UpdateView):
    model = AcademicSession

    form_class = AcademicSessionForm

    template_name = "academics/session/update.html"

    success_url = reverse_lazy("academics:session-list")
