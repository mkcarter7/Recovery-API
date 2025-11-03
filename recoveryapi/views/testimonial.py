from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Testimonial
from ..serializers import TestimonialSerializer


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for viewing testimonials"""
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured testimonials"""
        testimonials = self.queryset.filter(is_featured=True, is_active=True).order_by('order')
        serializer = self.get_serializer(testimonials, many=True)
        return Response(serializer.data)
