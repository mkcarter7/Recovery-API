from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import SiteContent
from ..serializers import SiteContentSerializer


class SiteContentViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for site content"""
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer
    lookup_field = 'content_type'

    @action(detail=False, methods=['get'])
    def all(self, request):
        """Get all site content as key-value pairs"""
        content = {}
        for item in self.queryset:
            content[item.content_type] = item.content
        return Response(content)
