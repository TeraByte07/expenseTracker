from recurring_app.models import recurring
from rest_framework import serializers

class recurringSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = recurring
        fields = ["user","recurring_type", "interval", "start_date", "end_date"]