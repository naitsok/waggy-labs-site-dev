from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, TextBlock, StructBlock
from .label import LabelBlock


class BlockQuoteBlock(StructBlock):
    """Quote block with text, author and source."""
    quote = TextBlock(
        required=True,
        help_text=_('Quote text.'),
        rows=3
    )
    author = CharBlock(
        required=False,
        help_text=_('Author of the quoted text.')
    )
    source = CharBlock(
        required=False,
        help_text=_('Source of the quoted text.')
    )
    label = LabelBlock(
        max_length=50,
        required=False
    )
    
    class Meta:
        icon = 'openquote'
        label = 'Quote'
        template = 'waggylabs/blocks/blockquote.html'