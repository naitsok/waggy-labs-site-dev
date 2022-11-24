from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import StructBlock

from .code import CodeBlock
from .mathjax_markdown import MathJaxMarkdownBlock
from .label import LabelBlock


class ListingBlock(StructBlock):
    """A code block with caption."""
    code = CodeBlock()
    caption = MathJaxMarkdownBlock(
        required=False,
        label=_('Listing caption'),
        help_text='',
        easymde_min_height='100px',
        easymde_max_height='100px',
        easymde_combine='true',
        easymde_toolbar_config=('bold,italic,strikethrough,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false',
    )
    label = LabelBlock(
        max_length=50,
        required=False,
        form_classname='waggylabs-label-listing', # needed to render references to listings
        )
    
    class Meta:
        icon='code'
        label='Code'
        template = 'waggylabs/blocks/listing.html'