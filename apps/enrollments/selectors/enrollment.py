from apps.enrollments.models.enrollment import StudentEnrollment


def get_active_enrollments():

    return StudentEnrollment.objects.select_related(
        "student",
        "session",
        "school_class",
    ).filter(status="ACTIVE")
