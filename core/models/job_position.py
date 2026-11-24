from django.db import models

from .department import Department


class JobPosition(models.Model):
    """An open role a candidate can be screened against."""

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="job_positions",
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    # A JSON list of required skills, e.g. ["Python", "Django", "SQL"].
    required_skills = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "job_positions"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} ({self.department.name})"
