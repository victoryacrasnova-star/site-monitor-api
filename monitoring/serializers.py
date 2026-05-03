from rest_framework import serializers
from .models import MonitoredSite, ParseResult

class MonitoredSiteSerializer(serializers.ModelSerializer):
    def validate_url(self, value):
        if not value.startswith("http://", "https://"):
            raise serializers.ValidationError(
                "URL must start with http:// or https://"
            )
        return value

    class Meta:
        model = MonitoredSite
        fields = '__all__'

class ParseResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParseResult
        fields = '__all__'