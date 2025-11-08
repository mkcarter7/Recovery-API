from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from recovery.authentication import FirebaseAuthentication
from ..models import Program, ProgramType
from ..serializers import ProgramSerializer, ProgramTypeSerializer


class ProgramTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Public API endpoint for viewing active program types."""

    queryset = ProgramType.objects.filter(is_active=True).order_by('order', 'name')
    serializer_class = ProgramTypeSerializer


class ProgramTypeAdminViewSet(viewsets.ModelViewSet):
    """Authenticated CRUD endpoint for managing program types."""

    queryset = ProgramType.objects.all().order_by('order', 'name')
    serializer_class = ProgramTypeSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """Public API endpoint for viewing active programs."""

    queryset = Program.objects.filter(is_active=True).select_related('program_type')
    serializer_class = ProgramSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured programs ordered by display priority."""
        programs = self.queryset.filter(is_active=True).order_by('order')[:3]
        serializer = self.get_serializer(programs, many=True)
        return Response(serializer.data)


class ProgramAdminViewSet(viewsets.ModelViewSet):
    """Authenticated CRUD endpoint for managing programs."""

    queryset = Program.objects.all().select_related('program_type').order_by('order', 'name')
    serializer_class = ProgramSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
