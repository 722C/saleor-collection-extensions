from django.utils.translation import npgettext, pgettext_lazy
from django_filters import (CharFilter, OrderingFilter)

from saleor.core.filters import SortedFilterSet

from ..models import CollectionExtension

SORT_BY_FIELDS = {
    'collection__name': pgettext_lazy('Collection list sorting option', 'name')}


class CollectionExtensionFilter(SortedFilterSet):
    collection__name = CharFilter(
        label=pgettext_lazy('Collection list filter label', 'Name'),
        lookup_expr='icontains')
    sort_by = OrderingFilter(
        label=pgettext_lazy('Collection list filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = CollectionExtension
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard collection extensions list',
            'Found %(counter)d matching collection extension',
            'Found %(counter)d matching collection extensions',
            number=counter) % {'counter': counter}
