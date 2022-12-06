from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (
    StreamBlock, StructBlock, CharBlock, ListBlock,
    BooleanBlock, ChoiceBlock
    )
from wagtail.embeds.blocks import EmbedBlock

from waggylabs.widgets.editor import DisabledOptionSelect

from .equation import EquationBlock
from .listing import ListingBlock
from .figure import FigureBlock
from .mathjax_markdown import MathJaxMarkdownBlock
from .table import TableBlock, TableFigureBlock


class AccordionContentBlock(StreamBlock):
    """Content block for one accordion item."""
    markdown = MathJaxMarkdownBlock(
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
    code = ListingBlock()
    figure = FigureBlock()
    embed = EmbedBlock(required=True)
    equation = EquationBlock()
    table_figure = TableFigureBlock()
    table = TableBlock()
    
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
    
    def render_form_template(self):
        self.child_blocks['heading'].field.widget.attrs.update({
            'placeholder': _('Heading of the item'),
        })
        return super().render_form_template()
    
    class Meta:
        icon = 'arrow-down-big'
        label = _('Item of the accordion')
        form_template = 'waggylabs/blocks/accordion_item.html'
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

    class Meta:
        icon = 'list-ul'
        label = _('Accordion')
        template = 'waggylabs/frontend_blocks/accordion.html'
        form_template = 'waggylabs/blocks/accordion.html'
        label_format = _('Accordion: {items}')
    