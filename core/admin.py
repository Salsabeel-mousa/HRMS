"""Register HR models so they can be managed from the Django admin site."""
from django.contrib import admin

from core.models import (
    Candidate,
    Department,
    InterviewQuestionSet,
    JobPosition,
    Resume,
    ScreeningResult,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "department", "created_at")
    list_filter = ("department",)
    search_fields = ("title", "description")
    list_select_related = ("department",)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "created_at")
    search_fields = ("full_name", "email", "phone")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "file", "uploaded_at")
    search_fields = ("candidate__full_name", "candidate__email")
    list_select_related = ("candidate",)


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "job_position", "score", "recommendation", "generated_at")
    list_filter = ("recommendation", "job_position")
    search_fields = ("candidate__full_name", "job_position__title")
    list_select_related = ("candidate", "job_position")


@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "job_position", "screening_result", "generated_at")
    list_filter = ("job_position",)
    search_fields = ("candidate__full_name", "job_position__title")
    list_select_related = ("candidate", "job_position")
