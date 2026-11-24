from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .candidate import Candidate
from .job_position import JobPosition


class ScreeningResult(models.Model):
    """
    Result of screening a candidate's resume against a job position.

    Holds the match score, strengths, missing skills and the final
    proceed / hold / reject recommendation. These records will later be
    produced by the AI screening agent; for now they are added via the admin.
    """

    class Recommendation(models.TextChoices):
        PROCEED = "proceed", "Proceed to Interview"
        HOLD = "hold", "Hold for Review"
        REJECT = "reject", "Reject"

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="screening_results",
    )
    job_position = models.ForeignKey(
        JobPosition,
        on_delete=models.CASCADE,
        related_name="screening_results",
    )
    # Match score from 0 to 100.
    score = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    # JSON lists of strings.
    strengths = models.JSONField(default=list, blank=True)
    missing_skills = models.JSONField(default=list, blank=True)
    recommendation = models.CharField(
        max_length=20,
        choices=Recommendation.choices,
        default=Recommendation.HOLD,
    )
    summary = models.TextField(blank=True)
    # The full, unmodified report (useful for debugging / audit).
    raw_report = models.JSONField(default=dict, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "screening_results"
        ordering = ["-generated_at"]

    def __str__(self) -> str:
        return f"Screening: {self.candidate.full_name} -> {self.job_position.title} ({self.score})"
