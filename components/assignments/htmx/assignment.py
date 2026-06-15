from django.shortcuts import render

from apps.assignments.forms.assignment_form import AssignmentForm


def assignment_modal(request):

    return render(
        request, "assignments/partials/modal.html", {"form": AssignmentForm()}
    )
