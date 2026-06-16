
from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report_card_pdf(
    report_card,
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Student Report Card", styles["Title"]))

    elements.append(Spacer(1, 20))

    elements.append(Paragraph(report_card.student.get_full_name(), styles["Normal"]))

    data = [
        [
            "Subject",
            "Score",
            "Grade",
        ]
    ]

    for subject in report_card.subjects.all():
        data.append(
            [
                str(subject.class_subject),
                str(subject.total),
                subject.grade,
            ]
        )

    elements.append(Table(data))

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf