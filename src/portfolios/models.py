from django.db import models


class Portfolio(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='portfolios')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    stock_records = models.ForeignKey('records.StockRecord', related_name='stock_records')
    fund_records = models.ForeignKey('records.FundRecord', related_name='fund_records')

    class Meta:
        verbose_name = 'portfolio'
        verbose_name_plural = 'portfolios'
        db_table = 'portfolios'
    
    @cached_property
    def amount(self):
        return self.portfolio.value

