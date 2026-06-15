from decimal import Decimal


def calculate_rubric_score(
    rubric_scores,
):

    total = Decimal("0")

    for score in rubric_scores:
        total += Decimal(score)

    return total
