from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import ScreeningResult
from core.serializers import ScreeningResultSerializer


# HRMS-117 — View Screening Result
@api_view(["GET"])
def get_screening_result(request, pk):
    """GET /api/screening-results/<int:pk>/"""
    try:
        screening = ScreeningResult.objects.get(pk=pk)
    except ScreeningResult.DoesNotExist:
        return Response(
            {"detail": "Screening result not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    return Response(ScreeningResultSerializer(screening).data, status=status.HTTP_200_OK)
