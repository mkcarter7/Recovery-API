from rest_framework import viewsets

from ..models import Feature
from ..serializers import FeatureSerializer


class FeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for viewing features/activities"""
    queryset = Feature.objects.filter(is_active=True)
    serializer_class = FeatureSerializer
