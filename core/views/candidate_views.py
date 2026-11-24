from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.serializers import CandidateSerializer


# HRMS-115 — Create Candidate
@api_view(["POST"])
def create_candidate(request):
    """POST /api/candidates/"""
    serializer = CandidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        serializer.save()
    except IntegrityError:
        # Safety net if two identical requests arrive at the same time.
        return Response(
            {"detail": "A candidate with this email already exists."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(serializer.data, status=status.HTTP_201_CREATED)
