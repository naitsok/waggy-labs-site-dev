from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, TextBlock, StructBlock


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
    anchor = CharBlock(
        max_length=50,
        required=False,
        help_text=_('Anchor link id for referencing in a Markdown block using #anchor.')
    )
    
    class Meta:
        icon = 'openquote'
        label = 'Quote'
        template = 'waggy_labs/blocks/blockquote.html'