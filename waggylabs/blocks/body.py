
from wagtail.blocks import StreamBlock
from wagtail.fields import StreamValue

from .accordion import AccordionBlock
from .blockquote import BlockQuoteBlock
from .card_grid import CardGridBlock
from .carousel import ImageCarouselBlock
from .collapse import CollapseBlock
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
    collapse = CollapseBlock()
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
    
    
    @classmethod
    def citation_blocks(cls, body: StreamValue):
        """Returns citation blocks (= citation and document)
         ordered by the appearance in the body
         StreamValue (body = StreamField(BodyBlock())) in a
         Page model."""
        citation_blocks = []
        for block in body:
            # Append all citation and document blocks
            if (block.block_type == 'citation'
                or block.block_type == 'document'):
                citation_blocks.append(block)
            
            # If block is accordion - loop through its child blocks
            # and append chitation and document blocks
            if block.block_type == 'accordion':
                citation_blocks = (citation_blocks +
                                   AccordionBlock.citation_blocks(block))
                
            # If block is collapse - loop through its child blocks
            # and append citation and document blocks
            if block.block_type == 'collapse':
                citation_blocks = (citation_blocks +
                                   CollapseBlock.citation_blocks(block))
            
            # If block is columns - loop through its child blocks
            # and append citation and document blocks
            if block.block_type == 'columns':
                citation_blocks = (citation_blocks +
                                   ColumnsBlock.citation_blocks(block))
        
        return citation_blocks
                
    