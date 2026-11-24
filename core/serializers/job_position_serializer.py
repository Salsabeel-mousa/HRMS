from rest_framework import serializers

from core.models import JobPosition


class JobPositionSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = JobPosition
        fields = [
            "id",
            "department",
            "department_name",
            "title",
            "description",
            "required_skills",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Title cannot be blank.")
        return value

    def validate_required_skills(self, value):
        """required_skills must be a list of non-empty strings, without duplicates."""
        if not isinstance(value, list):
            raise serializers.ValidationError("required_skills must be a list of strings.")

        cleaned, seen = [], set()
        for skill in value:
            if not isinstance(skill, str) or not skill.strip():
                raise serializers.ValidationError("Each skill must be a non-empty string.")
            skill = skill.strip()
            if skill.lower() not in seen:
                seen.add(skill.lower())
                cleaned.append(skill)
        return cleaned
