from django.urls import path
from .views.course_generator import GenerateCourseView





urlpatterns = [
    path(
        "generate-course/",
        GenerateCourseView.as_view(),
        name="generate-course",
    ),
]
