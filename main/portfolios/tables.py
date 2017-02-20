import itertools

import django_tables2 as tables
from django_tables2.tables import TableData
from django_tables2.utils import cached_property

from growthstreet.portfolios.models import Business
from utils.tables import ExtendedTable


class PortfolioTableData(TableData):

    @cached_property
    def verbose_name(self):
        return 'Portfolio'

    @cached_property
    def verbose_name_plural(self):
        return 'Portfolios'