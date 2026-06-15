from django.views.generic import (
    ListView,
    CreateView,
)

from django.urls import reverse_lazy

from apps.academics.models import Subject

from apps.academics.forms.subject import SubjectForm


class SubjectListView(ListView):
    model = Subject

    template_name = "academics/subject/list.html"

    context_object_name = "subjects"


class SubjectCreateView(CreateView):
    model = Subject

    form_class = SubjectForm

    template_name = "academics/subject/create.html"

    success_url = reverse_lazy("academics:subject-list")
