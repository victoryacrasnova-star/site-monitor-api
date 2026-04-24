from rest_framework import serializers
from .models import MonitoredSite, ParseResult

class MonitoredSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoredSite
        fields = '__all__'

class ParseResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParseResult
        fields = '__all__'