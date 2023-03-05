from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    ChoiceBlock, StructBlock, CharBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import (
    CardStyleChoiceBlock, HeaderStyleChoiceBlock
)
from waggylabs.widgets import DisabledOptionSelect


class PostCategoriesBlock(StructBlock):
    """Block to show post categories."""
    style = CardStyleChoiceBlock(
        required=False,
        label=_('Style')
    )
    header = CharBlock(
        required=False,
        label=_('Header'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('Header icon - start typing'),
    )
    header_icon_location = IconLocationBlock(
        required=False,
        label=_('Header icon location')
    )
    