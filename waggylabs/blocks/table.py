from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock

from .mathjax_markdown import MathJaxMarkdownBlock
from .label import LabelBlock


class TableFigureBlock(StructBlock):
    """Add Table as picture."""
    image = ImageChooserBlock(
        required=True,
        help_text=_('Choose an image'),
        )
    caption = MathJaxMarkdownBlock(
        required=False,
        help_text=_('Table caption'),
        easymde_min_height='150px',
        easymde_max_height='150px',
        easymde_combine='true',
        easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide'
    )
    label = LabelBlock(
        max_length=50,
        required=False,
        form_classname='waggylabs-label-table', # needed to render references to tables
    )
    
    class Meta:
        template = 'waggylabs/blocks/table_figure.html'
        icon = 'table'
        label = 'Table as picture'