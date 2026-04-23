from django.contrib import admin
from .models import MonitoredSite, ParseResult

# Register your models here.
admin.site.register(MonitoredSite)
admin.site.register(ParseResult)