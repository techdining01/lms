from django.db import transaction

from apps.enrollments.models.enrollment import StudentEnrollment


@transaction.atomic
def enroll_student(
    *,
    student,
    session,
    school_class,
    enrolled_by,
):

    return StudentEnrollment.objects.create(
        student=student,
        session=session,
        school_class=school_class,
        enrolled_by=enrolled_by,
    )
