from django.views.generic import (
    ListView,
    CreateView,
)

from django.urls import reverse_lazy

from apps.academics.models import SchoolClass

from apps.academics.forms.class_ import SchoolClassForm


class SchoolClassListView(ListView):
    model = SchoolClass

    template_name = "academics/class/list.html"

    context_object_name = "classes"


class SchoolClassCreateView(CreateView):
    model = SchoolClass

    form_class = SchoolClassForm

    template_name = "academics/class/create.html"

    success_url = reverse_lazy("academics:class-list")
