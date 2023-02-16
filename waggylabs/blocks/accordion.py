from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StreamBlock, StructBlock, CharBlock, ListBlock,
    BooleanBlock, ChoiceBlock, StructValue
    )

from waggylabs.widgets import DisabledOptionSelect

from .blockquote import BlockQuoteBlock
from .carousel import ImageCarouselBlock
from .citation import CitationBlock
from .document import DocumentBlock
from .embed import EmbedBlock
from .equation import EquationBlock
from .figure import FigureBlock
from .listing import ListingBlock
from .markdown import MarkdownBlock
from .table import TableBlock, TableFigureBlock


class AccordionContentBlock(StreamBlock):
    """Content block for one accordion item."""
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
    text = MarkdownBlock(
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
    
    class Meta:
        label = _('Body of the accordion item')
    

class AccordionItemBlock(StructBlock):
    """One accordion item block with heading."""
    heading = CharBlock(
        required=True,
        label=_('Item Heading'),
        classname='full subtitle'
    )
    is_open = BooleanBlock(
        required=False,
        label=_('Check if the item is displayed expanded')
    )
    body = AccordionContentBlock(
        required=True,
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['heading'].field.widget.attrs.update({
            'placeholder': _('Heading of the item'),
        })
    
    class Meta:
        icon = 'doc-full'
        label = _('Item of the accordion')
        form_template = 'waggylabs/blocks/form_template/accordion_item.html'
        label_format = '{heading}'


class AccordionBlock(StructBlock):
    """Accordion block in which multiple accordion items can 
    be added."""
    
    style = ChoiceBlock(
        choices=[
            ('', _('Choose item collapse style')),
            ('collapsible', _('Items collapse')),
            ('stays_open', _('Items stay open')),
        ],
        default='',
        label=_('Collapse items when new items opens or keep them open'),
        widget=DisabledOptionSelect
    )
    items = ListBlock(AccordionItemBlock())
    
    @classmethod
    def blocks_by_types(cls, accordion: StructValue, types: list):
        """Returns blocks specificed by types (e.g., citation and document)
         ordered by the appearance in the AccordionBlock StructValue."""
        blocks_by_types = []
        for accordion_item in accordion.value['items']:
            for acc_item_block in accordion_item['body']:
                if acc_item_block.block_type in types:
                    blocks_by_types.append(acc_item_block)
        return blocks_by_types

    class Meta:
        icon = 'list-ul'
        label = _('Accordion')
        template = 'waggylabs/blocks/template/accordion.html'
        form_template = 'waggylabs/blocks/form_template/accordion.html'
        label_format = _('Accordion: {items}')
    