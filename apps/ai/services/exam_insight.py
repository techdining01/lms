def generate_exam_insight(
    result,
):

    percentage = result.percentage

    if percentage >= 80:
        return "Excellent mastery."

    if percentage >= 60:
        return "Good performance."

    return "Needs improvement."
