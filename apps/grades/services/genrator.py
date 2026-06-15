from apps.grades.models import Gradebook

from apps.grades.services.calculator import calculate_grade


def generate_gradebook(
    *,
    student,
    class_subject,
    term,
    ca_score,
    exam_score,
):

    total = ca_score + exam_score

    grade_data = calculate_grade(total)

    return Gradebook.objects.create(
        student=student,
        class_subject=class_subject,
        term=term,
        ca_score=ca_score,
        exam_score=exam_score,
        total_score=total,
        grade=grade_data["grade"],
        remark=grade_data["remark"],
    )
