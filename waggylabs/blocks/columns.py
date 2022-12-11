
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import StreamBlock, StructBlock, ListBlock
from wagtail.embeds.blocks import EmbedBlock

from .accordion import AccordionBlock
from .blockquote import BlockQuoteBlock
from .carousel import ImageCarouselBlock
from .citation import CitationBlock
from .document import DocumentBlock
from .equation import EquationBlock
from .figure import FigureBlock
from .listing import ListingBlock
from .mathjax_markdown import MathJaxMarkdownBlock
from .table import TableBlock, TableFigureBlock


class ColumnBlock(StreamBlock):
    """Block to for one column."""
    accordion = AccordionBlock()
    blockquote = BlockQuoteBlock()
    carousel = ImageCarouselBlock()
    citation = CitationBlock()
    document = DocumentBlock()
    embed = EmbedBlock()
    equation = EquationBlock()
    figure = FigureBlock()
    listing = ListingBlock()
    table = TableBlock()
    table_figure = TableFigureBlock()
    text = MathJaxMarkdownBlock(help_text='')
    
    class Meta:
        icon = 'doc-empty'
        label = _('Column')
        

DEFAULT_MAX_COLUMNS = 3
class ColumnsBlock(StructBlock):
    """Block to add multiple columns."""
    columns = ListBlock(
        ColumnBlock(),
        min_num=1,
        max_num=(settings.WAGGYLABS_MAX_COLUMNS if
                 hasattr(settings, 'WAGGYLABS_MAX_COLUMNS')
                 else DEFAULT_MAX_COLUMNS),
    )
        
    class Meta:
        icon = 'duplicate'
        label = _('Multiple columns')
        template = 'waggylabs/frontend_blocks/columns.html'
        form_template = 'waggylabs/blocks/columns.html'
        label_format = _('Columns')