
from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

from waggylabs.widgets.editor import DEFAULT_FONTAWESOME_ICONS


register = template.Library()


ICONS = (settings.WAGGYLABS_FONTAWESOME_ICONS if
         hasattr(settings, 'WAGGYLABS_FONTAWESOME_ICONS')
         else DEFAULT_FONTAWESOME_ICONS)

@register.filter(name='is_icon')
@stringfilter
def is_icon(value):
    """Checks if valus is in icons keys."""
    return value in ICONS


@register.filter(name='icon_class')
@stringfilter
def icon_class(value):
    """Gets Font Awesome icon class from its name."""
    return ICONS[value]


@register.filter(name='link_https')
@stringfilter
def link_https(value):
    """Checks the presence of http and https."""
    value = value.lower()
    if not (value.startswith('http://') or value.startwith('https://')):
        value = 'https://' + value
    return value

@register.filter(name='col_class')
def col_class(value):
    """Calulates the correct value for Bootstrap CSS
    column width class."""
    return int(12 / len(value.bound_blocks))
    