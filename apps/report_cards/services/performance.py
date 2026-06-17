def student_growth(
    student,
):

    return student.reportcard_set.order_by("term__start_date")


