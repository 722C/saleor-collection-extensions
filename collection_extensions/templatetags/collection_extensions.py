from django import template

from ..models import CollectionExtension


register = template.Library()


@register.inclusion_tag('collection_extensions/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def collection_extensions_side_nav(context):
    return context


@register.filter
def collection_alternative_name(collection):
    if collection:
        ce = CollectionExtension.objects.filter(collection=collection).first()
        if ce:
            return ce.alternative_name
    return ''


@register.filter
def collection_content(collection):
    if collection:
        ce = CollectionExtension.objects.filter(collection=collection).first()
        if ce:
            return ce.content
    return ''
