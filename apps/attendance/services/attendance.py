from django.db import transaction

from apps.attendance.models.student_attendance import StudentAttendance


@transaction.atomic
def mark_attendance(
    *,
    student,
    school_class,
    status,
    date,
    marked_by,
):

    obj, created = StudentAttendance.objects.update_or_create(
        student=student,
        date=date,
        defaults={
            "school_class": school_class,
            "status": status,
            "marked_by": marked_by,
        },
    )

    return obj
