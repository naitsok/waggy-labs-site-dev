from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, StructBlock

from .code import CodeBlock
from .mathjax_markdown import MathJaxMarkdownBlock


class ListingBlock(StructBlock):
    """A code block with caption."""
    code = CodeBlock()
    caption = MathJaxMarkdownBlock(
        required=False,
        help_text=_('Listing caption'),
        easymde_min_height='150px',
        easymde_max_height='150px',
        easymde_combine='true',
        easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide',
    )
    anchor = CharBlock(
        max_length=50,
        required=False,
        help_text=_('Anchor link id for referencing in a Markdown block using #anchor.'),
    )
    
    class Meta:
        icon='code'
        label='Code'
        template = 'waggylabs/blocks/listing.html'