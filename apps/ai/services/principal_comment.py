def generate_principal_comment(
    average,
):

    if average >= 80:
        return "Outstanding result."

    if average >= 60:
        return "Satisfactory result."

    return "More effort required."
