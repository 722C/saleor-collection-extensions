from django import template

register = template.Library()


@register.inclusion_tag('collection_extensions/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def collection_extensions_side_nav(context):
    return context
