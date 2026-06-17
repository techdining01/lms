import mark_attendance


def bulk_mark_attendance(
    session,
    attendance_data,
):

    for item in attendance_data:
        mark_attendance(
            session=session,
            student=item["student"],
            status=item["status"],
        )
