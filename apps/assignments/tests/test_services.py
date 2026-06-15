from django.test import TestCase

from apps.assignments.services.late_submission import calculate_penalty


class LatePenaltyTest(TestCase):
    def test_penalty_applied(self):

        result = calculate_penalty(
            assignment=MockAssignment(),
            score=100,
        )

        self.assertEqual(result, 90)
