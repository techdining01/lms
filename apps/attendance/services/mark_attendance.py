from django.db import transaction

from apps.attendance.models import (
    AttendanceRecord,
)


@transaction.atomic
def mark_attendance(
    *,
    session,
    student,
    status,
):

    return AttendanceRecord.objects.update_or_create(
        session=session, student=student, defaults={"status": status}
    )
