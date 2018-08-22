from django import forms
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from saleor.product.models import Collection
from ..models import CollectionExtension


class CollectionExtensionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Collection.objects.all())

    class Meta:
        model = CollectionExtension
        verbose_name_plural = 'extended collections'
        exclude = []

    def __init__(self, *args, **kwargs):
        super(CollectionExtensionForm, self).__init__(*args, **kwargs)

        # Modify the queryset so that we don't show collections that are
        # already extended.
        # We need to do this differently for when the
        # user is adding vs editing so we can explicitly include the current
        # category when they are editing.
        if self.instance.pk:
            self.fields['category'].queryset = self.fields[
                'category'].queryset.filter(
                    Q(id=self.instance.category.pk) |
                    Q(extension__isnull=True))
        else:
            self.fields['category'].queryset = self.fields[
                'category'].queryset.filter(extension__isnull=True)
