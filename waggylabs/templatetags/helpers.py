from atexit import register
import uuid

from django import template

register = template.Library()

@register.simple_tag(takes_context=False)
def random_uuid():
    """Django template tag to generate unique identifier
    needed for the HTML element ids, e.g. in Carousel block.

    Returns:
        str: unique identifier
    """
    return str(uuid.uuid4())

