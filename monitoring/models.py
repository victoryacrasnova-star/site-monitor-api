from django.db import models

class MonitoredSite(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ParseResult(models.Model):
    site = models.ForeignKey(
        MonitoredSite,
        on_delete=models.CASCADE,
        related_name='parse_results',
    )
    title = models.CharField(max_length=255)
    status_code = models.IntegerField()

    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.site.name} - {self.checked_at}"
