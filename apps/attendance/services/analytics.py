def attendance_risk_level(
    percentage,
):

    if percentage < 50:
        return "HIGH"

    if percentage < 75:
        return "MEDIUM"

    return "LOW"



