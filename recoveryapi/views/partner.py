from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from recovery.authentication import FirebaseAuthentication
from ..models import Partner
from ..serializers import PartnerSerializer


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    """Public read-only endpoint for active partners."""

    queryset = Partner.objects.filter(is_active=True).order_by('order', 'name')
    serializer_class = PartnerSerializer


class PartnerAdminViewSet(viewsets.ModelViewSet):
    """Firebase-authenticated endpoint for managing partners."""

    queryset = Partner.objects.all().order_by('order', 'name')
    serializer_class = PartnerSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
