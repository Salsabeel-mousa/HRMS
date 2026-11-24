from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.serializers import DepartmentSerializer


# HRMS-113 — Create Department
@api_view(["POST"])
def create_department(request):
    """POST /api/departments/"""
    serializer = DepartmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        serializer.save()
    except IntegrityError:
        # Safety net if two identical requests arrive at the same time.
        return Response(
            {"detail": "A department with this name already exists."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(serializer.data, status=status.HTTP_201_CREATED)
