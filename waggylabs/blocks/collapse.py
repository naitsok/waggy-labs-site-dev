
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StreamBlock, StructBlock, ChoiceBlock, CharBlock,
    StructValue
)

from waggylabs.widgets import DisabledOptionSelect

from .blockquote import BlockQuoteBlock
from .carousel import ImageCarouselBlock
from .citation import CitationBlock
from .document import DocumentBlock
from .embed import EmbedBlock
from .equation import EquationBlock
from .figure import FigureBlock
from .icon import IconBlock, IconLocationBlock
from .styling import LinkStyleChoiceBlock
from .listing import ListingBlock
from .table import TableBlock, TableFigureBlock
from .markdown import MarkdownBlock


class CollapseContentBlock(StreamBlock):
    """Block to keep content of the collapse block."""
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
        label = _('Body of the collapse')
        
        
class CollapseBlock(StructBlock):
    """Collapse block to e.g. put content under spoiler."""
    text = CharBlock(
        required=False,
        label=_('Text on the button')
    )
    style = LinkStyleChoiceBlock()
    icon = IconBlock(required=False)
    icon_location = IconLocationBlock(required=False)
    body = CollapseContentBlock(requred=True)
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Text on the collapse button'),
        })
        
    @classmethod
    def blocks_by_types(cls, collapse: StructValue, types: list):
        """Returns blocks specificed by types (e.g., citation and document)
         ordered by the appearance in the CollapseBlock StructValue."""
        blocks_by_types = []
        for block in collapse.value['body']:
            if block.block_type in types:
                blocks_by_types.append(block)
        return blocks_by_types
        
    class Meta:
        icon = 'arrows-up-down'
        label = _('Collapse')
        form_template = 'waggylabs/blocks/form_template/collapse.html'
        template = 'waggylabs/blocks/template/collapse.html'
        label_format = _('Collapse: {text}')
