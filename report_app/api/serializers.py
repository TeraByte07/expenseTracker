from rest_framework import serializers
from report_app.models import report

class reportSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = report
        fields = ["id", "user", "title", "description", "start_date", "end_date", "total_expenses", "total_income", "net_savings","categories_summary"]
        read_only_fields = ["total_expenses", "total_income", "net_savings","categories_summary"]
        
    def create(self, validated_data):
        return report.objects.create(**validated_data)