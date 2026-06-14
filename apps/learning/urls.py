from django.urls import path

from .views.catalog import (
    CourseCatalogView,
    CourseDetailView,
)

app_name = "learning"

urlpatterns = [
    path(
        "courses/",
        CourseCatalogView.as_view(),
        name="catalog",
    ),
    path(
        "courses/<slug:slug>/",
        CourseDetailView.as_view(),
        name="detail",
    ),
]
