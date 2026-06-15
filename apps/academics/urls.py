from django.urls import path

from apps.academics.views.session import SessionListView, SessionCreateView
from apps.academics.views.subject import SubjectListView, SubjectCreateView
from apps.academics.views.class_ import SchoolClassListView, SchoolClassCreateView

app_name = "academics"

urlpatterns = [
    path(
        "sessions/",
        SessionListView.as_view(),
        name="session-list",
    ),
    path(
        "sessions/create/",
        SessionCreateView.as_view(),
        name="session-create",
    ),
    path(
        "subjects/",
        SubjectListView.as_view(),
        name="subject-list",
    ),
    path(
        "subjects/create/",
        SubjectCreateView.as_view(),
        name="subject-create",
    ),
    path(
        "classes/",
        SchoolClassListView.as_view(),
        name="class-list",
    ),
    path(
        "classes/create/",
        SchoolClassCreateView.as_view(),
        name="class-create",
    ),
]
