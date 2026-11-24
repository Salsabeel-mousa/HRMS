"""API routes for the core app (function-based views with @api_view)."""
from django.urls import path

from core import views

urlpatterns = [
    path("departments/", views.create_department, name="create-department"),
    path("job-positions/", views.create_job_position, name="create-job-position"),
    path("candidates/", views.create_candidate, name="create-candidate"),
    path("resumes/", views.upload_resume, name="upload-resume"),
    path(
        "screening-results/<int:pk>/",
        views.get_screening_result,
        name="view-screening-result",
    ),
    path(
        "interview-question-sets/<int:pk>/",
        views.get_interview_question_set,
        name="view-interview-questions",
    ),
]
