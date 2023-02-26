from django.utils.translation import gettext_lazy as _

from wagtail.blocks import StructBlock, CharBlock


class SeriesBlock(StructBlock):
    """Block to display contents for post series. E.g. main post
    and its subposts."""
    pass