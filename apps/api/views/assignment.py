from rest_framework.viewsets import ModelViewSet

from apps.assignments.models import Assignment

from apps.api.serializers.assignment import AssignmentSerializer


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()

    serializer_class = AssignmentSerializer
