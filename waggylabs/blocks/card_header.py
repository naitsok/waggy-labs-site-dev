from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    CharBlock, StructBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import HeaderStyleChoiceBlock

class CardHeaderBlock(StructBlock):
    """A general block to configure header for other blocks
    commonly used in page body, sidebar, footer."""
    header = CharBlock(
        required=False,
        label=_('Header text'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('Header icon'),
    )
    header_icon_location = IconLocationBlock(
        required=False,
        label=_('Header icon location'),
    )
    header_style = HeaderStyleChoiceBlock(
        required=False,
        label=_('Header style'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
            block.field.widget.attrs.update({
                'placeholder': block.label,
            })
    
    class Meta:
        icon = 'title'
        label = _('Header settings')
        template = 'waggylabs/blocks/template/card_header.html'
        form_template = 'waggylabs/blocks/form_template/card_header.html'