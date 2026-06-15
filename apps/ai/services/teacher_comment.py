def generate_teacher_comment(
    average,
):

    if average >= 80:
        return "Excellent performance. Keep it up."

    if average >= 60:
        return "Good performance. More consistency needed."

    return "Needs improvement."
