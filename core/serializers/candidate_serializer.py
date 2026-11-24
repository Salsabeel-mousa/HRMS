import re

from rest_framework import serializers

from core.models import Candidate

PHONE_PATTERN = re.compile(r"^\+?[0-9\s\-()]{7,30}$")


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "full_name", "email", "phone", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_full_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Full name cannot be blank.")
        return value

    def validate_email(self, value):
        value = value.strip().lower()
        if Candidate.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("A candidate with this email already exists.")
        return value

    def validate_phone(self, value):
        value = value.strip()
        if value and not PHONE_PATTERN.match(value):
            raise serializers.ValidationError(
                "Enter a valid phone number (digits, spaces, '+', '-' or parentheses)."
            )
        return value
