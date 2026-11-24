from rest_framework import serializers

from core.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "description", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Department name cannot be blank.")
        # Case-insensitive duplicate check ("HR" and "hr" are the same department).
        if Department.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("A department with this name already exists.")
        return value
