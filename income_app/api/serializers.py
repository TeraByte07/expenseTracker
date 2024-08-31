from rest_framework import serializers
from income_app.models import income

class incomeSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = income
        fields = "__all__"