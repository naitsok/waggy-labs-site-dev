from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (
    StreamBlock, StructBlock, CharBlock, ListBlock,
    BooleanBlock
    )
from wagtail.embeds.blocks import EmbedBlock

from .equation import EquationBlock
from .listing import ListingBlock
from .figure import FigureBlock
from .mathjax_markdown import MathJaxMarkdownBlock
from .table import TableBlock, TableFigureBlock


class AccordionContentBlock(StreamBlock):
    """Content block for one accordion item."""
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
    table = TableBlock()
    
    class Meta:
        label = 'Body of the accordion item'
    

class AccordionItemBlock(StructBlock):
    """One accordion item block with heading."""
    heading = CharBlock(
        required=True,
        label=_('Item Heading'),
        classname='full subtitle'
    )
    body = AccordionContentBlock(
        required=True
    )
    
    class Meta:
        icon = 'arrow-down-big'
        label = 'Item of the accordion'


class AccordionBlock(StructBlock):
    """Accordion block in which multiple accordion items can 
    be added."""
    keep_open = BooleanBlock(
        required=False,
        default=False,
        label=_('Always open'),
        help_text=_('If true, keeps accordion items always open, i.e. other items '
                    'do not collapse when an new one is opened.')
    )
    items = ListBlock(AccordionItemBlock())

    class Meta:
        icon = 'list-ul'
        label = 'Accordion'
        template = 'waggylabs/blocks/accordion.html'
    