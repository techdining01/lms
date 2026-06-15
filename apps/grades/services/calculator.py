from apps.grades.models import GradeScale


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
