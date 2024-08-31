from expense_app.models import expense
from rest_framework import serializers

class expenseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = expense
        fields = "__all__"