from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from recovery.authentication import FirebaseAuthentication
from ..models import SiteContent
from ..serializers import SiteContentSerializer


class SiteContentViewSet(viewsets.ReadOnlyModelViewSet):
    """Public read-only API endpoint for site content."""

    queryset = SiteContent.objects.all().order_by('content_type')
    serializer_class = SiteContentSerializer
    lookup_field = 'content_type'

    @action(detail=False, methods=['get'])
    def all(self, request):
        """Return all site content as a flat key-value payload."""
        return Response({item.content_type: item.content for item in self.get_queryset()})


class SiteContentAdminViewSet(viewsets.ModelViewSet):
    """Authenticated CRUD endpoint for managing site content entries."""

    queryset = SiteContent.objects.all().order_by('content_type')
    serializer_class = SiteContentSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'content_type'

    def get_object(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        obj, _created = SiteContent.objects.get_or_create(content_type=lookup_value)
        self.check_object_permissions(self.request, obj)
        return obj
