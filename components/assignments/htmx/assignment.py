from django.shortcuts import render


def assignment_modal(request):
    # Import form lazily to avoid app-loading order issues during autodiscovery
    from apps.assignments.forms.assignment_form import AssignmentForm

    return render(
        request, "assignments/partials/modal.html", {"form": AssignmentForm()}
    )
