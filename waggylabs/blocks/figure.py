from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock

from .mathjax_markdown import MathJaxMarkdownBlock


class FigureBlock(StructBlock):
    """Image with caption for StreamField."""
    image = ImageChooserBlock(
        required=True,
        help_text=_('Choose an image'),
        )
    caption = MathJaxMarkdownBlock(
        required=False,
        help_text=_('Figure caption'),
        easymde_min_height='150px',
        easymde_max_height='150px',
        easymde_combine='true',
        easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide'
    )
    anchor = CharBlock(
        max_length=50,
        required=False,
        help_text=_('Anchor link id for referencing in a Markdown block using #anchor.')
    )
    
    class Meta:
        template = 'waggylabs/blocks/figure.html'
        icon = 'image'
        label = 'Figure'