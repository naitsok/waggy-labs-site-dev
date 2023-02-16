
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import StreamBlock
from wagtail.fields import StreamValue

from .accordion import AccordionBlock
from .blockquote import BlockQuoteBlock
from .card_grid import CardGridBlock
from .carousel import ImageCarouselBlock
from .collapse import CollapseBlock
from .columns import ColumnsBlock
from .cut import CutBlock
from .document import DocumentBlock
from .citation import CitationBlock
from .embed import EmbedBlock
from .equation import EquationBlock
from .figure import FigureBlock
from .listing import ListingBlock
from .markdown import MarkdownBlock
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
    text = MarkdownBlock()
    
    
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
    
    def render(self, value, context):
        value = { 'body': value }
        value['literature'] = BodyBlock.blocks_by_types(
            value['body'],
            ['citation', 'document']
        )
        if context['page'].show_sidebar:
            value['modals'] = BodyBlock.blocks_by_types(
                value['body'],
                ['embed', 'equation', 'listing', 'figure', 'table', 'table_figure']
            )
        if 'page_in_list' in context:
            # page is rendered in the list, e.g. after search
            # we need to display blocks in page.body only those that before cut
            # other blocks may be rendereded truncated, for example, to avoid image 
            # loading and use of traffic
            # however, literature, equations and all label blocks must be rendered
            # hidden in order to correctly generate reference and citations
            before_cut = []
            after_cut = []
            cut_met = False
            for block in value['body']:
                if not cut_met:
                    before_cut.append(block)
                else:
                    after_cut.append(block)
                if block.block_type == 'cut':
                    cut_met = True
            value['before_cut'] = before_cut
            value['after_cut'] = after_cut
            
        return super().render(value, context)
    
    class Meta:
        icon = 'doc'
        label = _('Page content')
        template = 'waggylabs/blocks/template/body.html'
                
    