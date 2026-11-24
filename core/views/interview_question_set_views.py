from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import InterviewQuestionSet
from core.serializers import InterviewQuestionSetSerializer


# HRMS-118 — View Interview Questions
@api_view(["GET"])
def get_interview_question_set(request, pk):
    """GET /api/interview-question-sets/<int:pk>/"""
    try:
        question_set = InterviewQuestionSet.objects.get(pk=pk)
    except InterviewQuestionSet.DoesNotExist:
        return Response(
            {"detail": "Interview question set not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    return Response(
        InterviewQuestionSetSerializer(question_set).data, status=status.HTTP_200_OK
    )
