from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import NewsletterSubscriber
from ..serializers import NewsletterSubscriberSerializer, NewsletterSubscriberAdminSerializer


class NewsletterSubscriberView(APIView):
    """API endpoint for newsletter subscriptions"""
    def post(self, request):
        serializer = NewsletterSubscriberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber = serializer.save()
            return Response(
                {'message': 'Successfully subscribed to newsletter!'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsletterSubscriberAdminViewSet(ReadOnlyModelViewSet):
    """Admin API endpoint for viewing newsletter subscriptions"""
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberAdminSerializer
