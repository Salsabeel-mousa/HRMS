from django.db import models


class Candidate(models.Model):
    """A person applying for a job position."""

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "candidates"
        ordering = ["full_name"]

    def __str__(self) -> str:
        return self.full_name
