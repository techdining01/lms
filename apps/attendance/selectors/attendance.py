from apps.attendance.models import StudentAttendance


def attendance_today():

    from django.utils import timezone

    return StudentAttendance.objects.filter(date=timezone.now().date())
