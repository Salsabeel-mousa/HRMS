from django.db import models


class Department(models.Model):
    """A department that owns one or more job positions (e.g. Engineering, HR)."""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "departments"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
