from apps.course_delivery.models.course import AcademicCourse


def published_courses():

    return AcademicCourse.objects.filter(is_published=True).select_related(
        "class_subject",
        "class_subject__teacher",
    )
