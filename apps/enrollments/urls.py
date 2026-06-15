from django.urls import path

from apps.enrollments.views.enrollment import EnrollmentListView, EnrollmentCreateView

app_name = "enrollments"

urlpatterns = [
    path(
        "",
        EnrollmentListView.as_view(),
        name="list",
    ),
    path(
        "create/",
        EnrollmentCreateView.as_view(),
        name="create",
    ),
]
