
from wagtail.blocks import StreamBlock

from .accordion import AccordionBlock
from .blockquote import BlockQuoteBlock
from .card_grid import CardGridBlock
from .carousel import ImageCarouselBlock
from .columns import ColumnsBlock
from .document import DocumentBlock
from .citation import CitationBlock
from .embed import EmbedBlock
from .equation import EquationBlock
from .figure import FigureBlock
from .listing import ListingBlock
from .mathjax_markdown import MathJaxMarkdownBlock
from .table import TableBlock, TableFigureBlock


class BodyBlock(StreamBlock):
    """General body field to add content to site pages and
     post pages."""
    accordion = AccordionBlock()
    blockquote = BlockQuoteBlock()
    card_grid = CardGridBlock()
    carousel = ImageCarouselBlock()
    columns = ColumnsBlock()
    citation = CitationBlock()
    document = DocumentBlock()
    embed = EmbedBlock()
    equation = EquationBlock()
    figure = FigureBlock()
    listing = ListingBlock()
    table = TableBlock()
    table_figure = TableFigureBlock()
    text = MathJaxMarkdownBlock()
    