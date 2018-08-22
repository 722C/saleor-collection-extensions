from django.db import models

from django.utils.translation import pgettext_lazy

from saleor.core.permissions import MODELS_PERMISSIONS


# Add in the permissions specific to our models.
MODELS_PERMISSIONS += [
    'collection_extensions.view',
    'collection_extensions.edit'
]


class CollectionExtension(models.Model):
    collection = models.OneToOneField(
        'product.Collection', on_delete=models.CASCADE,
        related_name='extension')
    alternative_name = models.CharField(max_length=255, blank=True)
    content = models.TextField(help_text=pgettext_lazy(
        'Collection extension', 'CMS-able content.'), blank=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'collection_extensions'

        permissions = (
            ('view', pgettext_lazy('Permission description',
                                   'Can view collection extensions')
             ),
            ('edit', pgettext_lazy('Permission description',
                                   'Can edit collection extensions')))

    def __str__(self):
        return self.collection.name
