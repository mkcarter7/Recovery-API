from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Program
from ..serializers import ProgramSerializer


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for viewing programs"""
    queryset = Program.objects.filter(is_active=True)
    serializer_class = ProgramSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured programs"""
        programs = self.queryset.filter(is_active=True).order_by('order')[:3]
        serializer = self.get_serializer(programs, many=True)
        return Response(serializer.data)
