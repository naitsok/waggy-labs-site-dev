
from wagtail.blocks import StreamBlock
from wagtail.embeds.blocks import EmbedBlock

from waggylabs.blocks.accordion import AccordionBlock
from waggylabs.blocks.blockquote import BlockQuoteBlock
from waggylabs.blocks.card_grid import CardGridBlock
from waggylabs.blocks.carousel import ImageCarouselBlock
from waggylabs.blocks.columns import ColumnsBlock
from waggylabs.blocks.citation import CitationBlock
from waggylabs.blocks.equation import EquationBlock
from waggylabs.blocks.figure import FigureBlock
from waggylabs.blocks.listing import ListingBlock
from waggylabs.blocks.mathjax_markdown import MathJaxMarkdownBlock
from waggylabs.blocks.table import TableBlock, TableFigureBlock


class BodyBlock(StreamBlock):
    """General body field to add content to site pages and
     post pages."""
    accordion = AccordionBlock()
    blockquote = BlockQuoteBlock()
    card_grid = CardGridBlock()
    columns = ColumnsBlock()
    citation = CitationBlock()
    embed = EmbedBlock()
    equation = EquationBlock()
    figure = FigureBlock()
    listing = ListingBlock()
    table = TableBlock()
    table_figure = TableFigureBlock()
    text = MathJaxMarkdownBlock()
    