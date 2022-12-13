from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (
    CharBlock, TextBlock, StructBlock, ChoiceBlock
)

from waggylabs.widgets import DisabledOptionSelect

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
    text_justify = ChoiceBlock(
        choices=[
            ('', _('Choose text alignment')),
            ('text-start', _('Left')),
            ('text-center', _('Center')),
            ('text-end', _('Right')),
        ],
        default='',
        label=_('Text alignment'),
        widget=DisabledOptionSelect,
    )
    
    class Meta:
        icon = 'openquote'
        label = _('Quote')
        template = 'waggylabs/frontend_blocks/blockquote.html'
        label_format = _('Quote: {quote}')