from rest_framework import serializers

from core.models import Resume
from core.models.resume import ALLOWED_RESUME_EXTENSIONS

MAX_RESUME_SIZE_MB = 5


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "candidate", "file", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]

    def validate_file(self, value):
        """Only accept resume file types we can read, up to a size limit."""
        allowed = tuple(f".{ext}" for ext in ALLOWED_RESUME_EXTENSIONS)
        if not value.name.lower().endswith(allowed):
            raise serializers.ValidationError(
                f"Unsupported file type. Allowed: {', '.join(allowed)}"
            )
        if value.size == 0:
            raise serializers.ValidationError("The uploaded file is empty.")
        if value.size > MAX_RESUME_SIZE_MB * 1024 * 1024:
            raise serializers.ValidationError(
                f"File too large. Maximum size is {MAX_RESUME_SIZE_MB} MB."
            )
        return value
