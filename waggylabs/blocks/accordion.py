from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (StreamBlock, StructBlock, CharBlock, ListBlock)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from .equation import EquationBlock
from .listing import ListingBlock
from .figure import FigureBlock
from .mathjax_markdown import MathJaxMarkdownBlock
from .table import TableBlock, TableFigureBlock


class AccordionContentBlock(StreamBlock):
    """Content block for one accordion item."""
    # heading = CharBlock(classname='full subtitle', required=True),
    markdown = MathJaxMarkdownBlock(
        required=False,
        help_text='',
        easymde_combine='true',
        easymde_min_height='150px',
        easymde_max_height='150px',
        easymde_toolbar_config=('bold,italic,strikethrough,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false'
        )
    code = ListingBlock()
    figure = FigureBlock()
    embed = EmbedBlock(required=True)
    equation = EquationBlock()
    table_figure = TableFigureBlock()
    table = TableBlock(),
    