
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
    def blocks_by_types(cls, body: StreamValue, types: list):
        """Returns blocks specificed by types (e.g., citation and document)
         ordered by the appearance in the body StreamValue 
         (body = StreamField(BodyBlock())) in a Page model."""
        blocks_by_types = []
        for block in body:
            # Append all citation and document blocks
            if block.block_type in types:
                blocks_by_types.append(block)
            
            # If block is accordion - loop through its child blocks
            # and append the specified types of blocks
            if block.block_type == 'accordion':
                blocks_by_types = (blocks_by_types +
                                   AccordionBlock.blocks_by_types(block, types))
                
            # If block is collapse - loop through its child blocks
            # and append the specified types of blocks
            if block.block_type == 'collapse':
                blocks_by_types = (blocks_by_types +
                                   CollapseBlock.blocks_by_types(block, types))
            
            # If block is columns - loop through its child blocks
            # and append the specified types of blocks
            if block.block_type == 'columns':
                blocks_by_types = (blocks_by_types +
                                   ColumnsBlock.blocks_by_types(block, types))
        
        return blocks_by_types
                
    