def calculate_percentage(
    score,
    total_marks,
):

    if total_marks == 0:
        return 0

    return (score / total_marks) * 100
