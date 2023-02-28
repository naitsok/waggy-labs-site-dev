
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StreamBlock, StructBlock, ListBlock, ChoiceBlock,
    StructValue
)

from waggylabs.widgets import DisabledOptionSelect

from waggylabs.blocks.accordion import AccordionBlock
from waggylabs.blocks.blockquote import BlockQuoteBlock
from waggylabs.blocks.carousel import ImageCarouselBlock
from waggylabs.blocks.citation import CitationBlock
from waggylabs.blocks.collapse import CollapseBlock
from waggylabs.blocks.document import DocumentBlock
from waggylabs.blocks.embed import EmbedBlock
from waggylabs.blocks.equation import EquationBlock
from waggylabs.blocks.figure import FigureBlock
from waggylabs.blocks.listing import ListingBlock
from waggylabs.blocks.markdown import MarkdownBlock
from waggylabs.blocks.table import TableBlock, TableFigureBlock


class ColumnsContentBlock(StreamBlock):
    """Block to for one column content."""
    accordion = AccordionBlock()
    blockquote = BlockQuoteBlock()
    carousel = ImageCarouselBlock()
    citation = CitationBlock()
    collapse = CollapseBlock()
    document = DocumentBlock()
    embed = EmbedBlock()
    equation = EquationBlock()
    figure = FigureBlock()
    listing = ListingBlock()
    table = TableBlock()
    table_figure = TableFigureBlock()
    text = MarkdownBlock(help_text='')
        

class ColumnsItemBlock(StructBlock):
    """Block for one column content and settings."""
    vertical_align = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Vertical alignment')),
            ('align-self-start', _('Top')),
            ('align-self-center', _('Center')),
            ('align-self-end', _('Bottom')),
        ]
    )
    body = ColumnsContentBlock(required=True)
    
    class Meta:
        icon = 'doc-full'
        label = _('Column')
        label_format = _('Column: {body}')
        

DEFAULT_MAX_COLUMNS = 3
class ColumnsBlock(StructBlock):
    """Block to add multiple columns."""
    items = ListBlock(
        ColumnsItemBlock(),
        min_num=1,
        max_num=(settings.WAGGYLABS_MAX_COLUMNS if
                 hasattr(settings, 'WAGGYLABS_MAX_COLUMNS')
                 else DEFAULT_MAX_COLUMNS),
    )
    
    @classmethod
    def blocks_by_types(cls, columns: StructValue, types: list):
        """Returns blocks specificed by types (e.g., citation and document)
         ordered by the appearance in the ColumnsBlock StructValue."""
        blocks_by_types = []
        for columns_item in columns.value['items']:
            for col_item_block in columns_item['body']:
                if col_item_block.block_type in types:
                    blocks_by_types.append(col_item_block)
                if col_item_block.block_type == 'accordion':
                    blocks_by_types = (blocks_by_types +
                                       AccordionBlock.blocks_by_types(col_item_block, types))
                if col_item_block.block_type == 'collapse':
                    blocks_by_types = (blocks_by_types +
                                       CollapseBlock.blocks_by_types(col_item_block, types))
        return blocks_by_types
        
    class Meta:
        icon = 'duplicate'
        label = _('Multiple columns')
        template = 'waggylabs/blocks/template/columns.html'
        form_template = 'waggylabs/blocks/form_template/columns.html'
        label_format = _('Columns: {items}')