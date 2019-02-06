from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from saleor.core.utils import get_paginator_items
from saleor.dashboard.views import staff_member_required
from .filters import CollectionExtensionFilter
from .forms import CollectionExtensionForm

from ..models import CollectionExtension


@staff_member_required
@permission_required('collection_extensions.view')
def collection_extension_list(request):
    collection_extensions = (
        CollectionExtension.objects.all().select_related('collection')
        .order_by('collection'))
    collection_extension_filter = CollectionExtensionFilter(
        request.GET, queryset=collection_extensions)
    collection_extensions = get_paginator_items(
        collection_extension_filter.qs, settings.DASHBOARD_PAGINATE_BY, request.GET.get('page'))
    # Call this so that cleaned_data exists on the filter_set
    collection_extension_filter.form.is_valid()
    ctx = {
        'collection_extensions': collection_extensions, 'filter_set': collection_extension_filter,
        'is_empty': not collection_extension_filter.queryset.exists()}
    return TemplateResponse(request, 'collection_extensions/dashboard/list.html', ctx)


@staff_member_required
@permission_required('collection_extensions.edit')
def collection_extension_create(request):
    collection_extension = CollectionExtension()
    form = CollectionExtensionForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy('Dashboard message',
                            'Created collection extension')
        messages.success(request, msg)
        return redirect('collection-extension-dashboard-list')
    ctx = {'collection_extension': collection_extension, 'form': form}
    return TemplateResponse(request, 'collection_extensions/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('collection_extensions.edit')
def collection_extension_details(request, pk):
    collection_extension = CollectionExtension.objects.get(pk=pk)
    form = CollectionExtensionForm(
        request.POST or None, instance=collection_extension)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Updated collection extension %s') % collection_extension.name
        messages.success(request, msg)
        return redirect('collection-extension-dashboard-list')
    ctx = {'collection_extension': collection_extension, 'form': form}
    return TemplateResponse(request, 'collection_extensions/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('collection_extensions.edit')
def collection_extension_delete(request, pk):
    collection_extension = get_object_or_404(CollectionExtension, pk=pk)
    if request.method == 'POST':
        collection_extension.delete()
        msg = pgettext_lazy('Dashboard message',
                            'Removed collection extension %s') % collection_extension
        messages.success(request, msg)
        return redirect('collection-extension-dashboard-list')
    return TemplateResponse(
        request, 'collection_extensions/dashboard/modal/confirm_delete.html', {'collection_extension': collection_extension})
