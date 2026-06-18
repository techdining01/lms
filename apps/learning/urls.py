from django.urls import path

from apps.learning.views.catalog import (
    CourseCatalogView,
)

from apps.learning.views.player import (
    CoursePlayerView,
)

urlpatterns = [
    path(
        "",
        CourseCatalogView.as_view(),
        name="catalog",
    ),  
    
    path(
        "courses/<slug:slug>/learn/",
        CoursePlayerView.as_view(),
        name="course-player",
    ),

]


 