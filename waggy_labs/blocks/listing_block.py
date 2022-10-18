from cProfile import label
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, StructBlock

from .code_block import CodeBlock
from .mathjax_markdown_block import MathJaxMarkdownBlock


class ListingBlock(StructBlock):
    """A code block with caption."""
    code = CodeBlock()
    caption = MathJaxMarkdownBlock(
        required=False,
        help_text=_('Listing caption'),
        easymde_min_height='200px',
        easymde_max_height='200px',
        easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,preview,side-by-side,fullscreen,guide',
    )
    anchor = CharBlock(
        max_length=50,
        required=False,
        help_text=_('Anchor link id for referencing in a Markdown block using #anchor.')
    )
    
    class Meta:
        icon='code'
        label='Code'
        template = 'waggy_labs/blocks/listing.html'