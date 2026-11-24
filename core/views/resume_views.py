from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from core.serializers import ResumeSerializer


# HRMS-116 — Upload Resume
@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_resume(request):
    """
    POST /api/resumes/  (multipart/form-data)

    Form fields:
        candidate : id of an existing candidate
        file      : .pdf, .docx or .txt file (max 5 MB)
    """
    serializer = ResumeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
