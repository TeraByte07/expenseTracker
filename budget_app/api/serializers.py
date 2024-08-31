from rest_framework import serializers
from budget_app.models import budget

class budgetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = budget
        fields = "__all__"