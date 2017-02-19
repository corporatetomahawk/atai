from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.functional import cached_property

class BaseRecord(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='record')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

class StockRecord(BaseRecord):
    EPIC_code = models.CharField(max_length=4)

class FundRecord(BaseRecord):
    SEDOL_code = models.IntegerField()