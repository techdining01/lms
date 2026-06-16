from apps.grades.models import GradeScale

def calculate_grade(
    score,
):
    if score >= 75:
        return "A", "Excellent"

    if score >= 65:
        return "B", "Very Good"

    if score >= 55:
        return "C", "Good"

    if score >= 45:
        return "D", "Fair"

    if score >= 40:
        return "E", "Pass"

    return "F", "Fail"


def calculate_total(
    *,
    assignment,
    ca,
    exam,
):
    return assignment + ca + exam


def calculate_grade(total_score):

    scale = GradeScale.objects.filter(
        min_score__lte=total_score,
        max_score__gte=total_score,
    ).first()

    if not scale:
        return None

    return {
        "grade": scale.grade,
        "remark": scale.remark,
    }
