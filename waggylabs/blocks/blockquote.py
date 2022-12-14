from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (
    CharBlock, StructBlock, ChoiceBlock, BooleanBlock
)

from waggylabs.widgets import DisabledOptionSelect

from .label import LabelBlock
from .mathjax_markdown import MathJaxMarkdownBlock


class BlockQuoteBlock(StructBlock):
    """Quote block with text, author and source."""
    quote = MathJaxMarkdownBlock(
        required=True,
        label=_('Quote text.'),
        help_text='',
        easymde_min_height='100px',
        easymde_max_height='100px',
        easymde_combine='true',
        easymde_toolbar_config=('bold,italic,strikethrough,heading,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false',
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
    show_icon = BooleanBlock(
        required=False,
        label=_('Show quote icon'),
    )
    
    class Meta:
        icon = 'openquote'
        label = _('Quote')
        template = 'waggylabs/frontend_blocks/blockquote.html'
        label_format = _('Quote: {quote}')