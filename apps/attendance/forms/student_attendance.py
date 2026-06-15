from django import forms

from apps.attendance.models.student_attendance import StudentAttendance


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance

        fields = [
            "student",
            "status",
        ]
