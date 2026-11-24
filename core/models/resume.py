from django.core.validators import FileExtensionValidator
from django.db import models

from .candidate import Candidate

ALLOWED_RESUME_EXTENSIONS = ["pdf", "docx", "txt"]


class Resume(models.Model):
    """An uploaded resume file belonging to a candidate."""

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="resumes",
    )
    # Files are stored under MEDIA_ROOT/resumes/
    file = models.FileField(
        upload_to="resumes/",
        validators=[FileExtensionValidator(ALLOWED_RESUME_EXTENSIONS)],
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "resumes"
        ordering = ["-uploaded_at"]

    def __str__(self) -> str:
        return f"Resume of {self.candidate.full_name} ({self.uploaded_at:%Y-%m-%d})"
