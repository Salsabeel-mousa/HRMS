from rest_framework import serializers

from core.models import ScreeningResult


class ScreeningResultSerializer(serializers.ModelSerializer):
    recommendation_display = serializers.CharField(
        source="get_recommendation_display", read_only=True
    )

    class Meta:
        model = ScreeningResult
        fields = [
            "id",
            "candidate",
            "job_position",
            "score",
            "strengths",
            "missing_skills",
            "recommendation",
            "recommendation_display",
            "summary",
            "generated_at",
        ]
        read_only_fields = fields
