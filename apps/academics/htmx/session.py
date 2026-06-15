from django.shortcuts import render

from apps.academics.forms.session import AcademicSessionForm


def session_modal(request):

    form = AcademicSessionForm()

    return render(
        request,
        "academics/partials/session_form.html",
        {"form": form},
    )

