from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, TextBlock, StructBlock
from .label import LabelBlock


class BlockQuoteBlock(StructBlock):
    """Quote block with text, author and source."""
    quote = TextBlock(
        required=True,
        label=_('Quote text.'),
        rows=3
    )
    author = CharBlock(
        required=False,
        label=_('Author of the quoted text.')
    )
    source = CharBlock(
        required=False,
        label=_('Source of the quoted text.')
    )
    label = LabelBlock(
        max_length=50,
        required=False,
        form_classname='waggylabs-label-blockquote',
    )
    
    class Meta:
        icon = 'openquote'
        label = _('Quote')
        template = 'waggylabs/frontend_blocks/blockquote.html'