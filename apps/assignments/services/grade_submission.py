def apply_late_penalty(
    score,
    penalty_percentage,
):

    deduction = (score * penalty_percentage) / 100

    return score - deduction

