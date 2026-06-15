from django.urls import path

from apps.assignments.views.assignment import (
    AssignmentListView,
    AssignmentCreateView,
    AssignmentDetailView,
)

from apps.assignments.views.submission import (
    SubmitAssignmentView
)

from apps.assignments.views.grading import GradeSubmissionView,


app_name = "assignments"

urlpatterns = [
    path(
        "",
        AssignmentListView.as_view(),
        name="list",
    ),
    path(
        "create/",
        AssignmentCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/",
        AssignmentDetailView.as_view(),
        name="detail",
    ),
    path(
        "<int:pk>/submit/",
        SubmitAssignmentView.as_view(),
        name="submit",
    ),
    path(
        "submission/<int:pk>/grade/",
        GradeSubmissionView.as_view(),
        name="grade-submission",
    ),
]
