from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from recovery.authentication import FirebaseAuthentication
from ..models import TeamMember
from ..serializers import TeamMemberSerializer


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """Public read-only endpoint for active team members."""

    queryset = TeamMember.objects.filter(is_active=True).order_by('order', 'name')
    serializer_class = TeamMemberSerializer


class TeamMemberAdminViewSet(viewsets.ModelViewSet):
    """Firebase-authenticated endpoint for managing team members."""

    queryset = TeamMember.objects.all().order_by('order', 'name')
    serializer_class = TeamMemberSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
