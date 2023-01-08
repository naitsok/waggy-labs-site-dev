
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
from .listing import ListingBlock
from .table import TableBlock, TableFigureBlock
from .mathjax_markdown import MathJaxMarkdownBlock


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
    text = MathJaxMarkdownBlock(
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
        required=True,
        label=_('Text on the button')
    )
    style = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose button style')),
            ('btn btn-link', _('Link')),
            ('btn btn-primary', _('Button primary')),
            ('btn btn-secondary', _('Button secondary')),
            ('btn btn-light', _('Button light')),
            ('btn btn-dark', _('Button dark')),
            ('btn btn-success', _('Button success')),
            ('btn btn-danger', _('Button danger')),
            ('btn btn-warning', _('Button warning')),
            ('btn btn-info', _('Button info')),
            ('btn btn-outline-primary', _('Button outline primary')),
            ('btn btn-outline-secondary', _('Button outline secondary')),
            ('btn btn-outline-light', _('Button outline light')),
            ('btn btn-outline-dark', _('Button outline dark')),
            ('btn btn-outline-success', _('Button outline success')),
            ('btn btn-outline-danger', _('Button outline danger')),
            ('btn btn-outline-warning', _('Button outline warning')),
            ('btn btn-outline-info', _('Button outline info')),
            ],
        default='',
        label=_('Style of the button'),
        widget=DisabledOptionSelect
    )
    body = CollapseContentBlock(requred=True)
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Text on the collapse button'),
        })
        
    @classmethod
    def citation_blocks(cls, collapse: StructValue):
        """Returns citation blocks (= citation and document)
         ordered by the appearance in the CollapseBlock
         StructValue."""
        citation_blocks = []
        for block in collapse.value['body']:
            if (block.block_type == 'citation'
                or block.block_type == 'document'):
                citation_blocks.append(block)
        return citation_blocks
        
    class Meta:
        icon = 'arrows-up-down'
        label = _('Collapse')
        form_template = 'waggylabs/blocks/collapse.html'
        template = 'waggylabs/frontend_blocks/collapse.html'
        label_format = _('Collapse: {text}')
