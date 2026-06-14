urlpatterns = [
    path(
        "instructor/",
        InstructorDashboardView.as_view(),
        name="instructor-dashboard",
    ),
    path(
        "instructor/courses/",
        InstructorCourseListView.as_view(),
        name="instructor-courses",
    ),
    path(
        "instructor/courses/create/",
        CourseCreateView.as_view(),
        name="course-create",
    ),
]
