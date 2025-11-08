from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from recovery.authentication import FirebaseAuthentication
from ..models import ContactSubmission
from ..serializers import ContactSubmissionSerializer, ContactSubmissionAdminSerializer


class ContactSubmissionView(APIView):
    """API endpoint for submitting contact forms"""

    def post(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Thank you for your message. We will get back to you soon.'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactSubmissionAdminViewSet(ReadOnlyModelViewSet):
    """Admin API endpoint for viewing contact form submissions"""

    queryset = ContactSubmission.objects.all().order_by('-created_at')
    serializer_class = ContactSubmissionAdminSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
