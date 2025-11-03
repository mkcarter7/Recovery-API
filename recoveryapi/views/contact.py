from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import ContactSubmissionSerializer


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
