from django.utils.translation import gettext_lazy as _

from wagtail.blocks import StructBlock, CharBlock, ChoiceBlock

from waggylabs.blocks.card_header import CardHeaderBlock
from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import (
    LinkStyleChoiceBlock, CardStyleChoiceBlock, TextAlignmentChoiceBlock,
    HeaderStyleChoiceBlock
)


class WrapperBlock(StructBlock):
    """Wrapper block for holding different blocks."""
    header = CharBlock(
        required=False,
        label=_('Header text'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('Header icon'),
    )
    header_icon_location = IconLocationBlock(
        required=False,
        label=_('Header icon location'),
    )
    header_style = HeaderStyleChoiceBlock(
        required=False,
        label=_('Header style'),
    )
    block_style = CardStyleChoiceBlock()
    block_alignment = TextAlignmentChoiceBlock()
    item = None
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        if self.child_blocks['item'] is None:
            raise ValueError('Wrapper block cannot be used on its own. '
                             'It must be subclassed to provide non-None item '
                             'instance.')
            
    class Meta:
        icon = 'form'
        label = _('Wrapper block')
        # form_template = 'waggylabs/blocks/form_template/wrapper.html'
        template = 'waggylabs/blocks/template/wrapper.html'
        
        

class PostSeriesBlockItem(StructBlock):
    """Block to display contents for post series. E.g. main post
    and its subposts."""
    post_link_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Post link style'),
    )
    current_post_style = ChoiceBlock(
        required=False,
        choices=[
            ('', 'Default'),
            ('fw-bold', 'Bold'),
            ('fw-bolder', 'Bolder'),
            ('fw-semibold', 'Semibold'),
            ('fw-normal', 'Normal'),
            ('fw-light', 'Light'),
            ('fw-lighter', 'Lighter'),
            ('fst-italic', 'Italic'),
            ('fw-bold fst-italic', 'Bold italic'),
            ('fw-bolder fst-italic', 'Bolder italic'),
            ('fw-semibold fst-italic', 'Semibold italic'),
            ('fw-light fst-italic', 'Light italic'),
            ('fw-lighter fst-italic', 'Lighter italic'),
        ],
        default='',
        label=_('Current post style'),
    )

    class Meta:
        label = _('Post series ONE')
        # form_template = 'waggylabs/blocks/form_template/post_series.html'
        template = 'waggylabs/blocks/template/post_series_item.html'
        help_text = _('If the post is included into a series, '
                      'its title appears in this block.')
        

class PostSeries1Block(WrapperBlock):
    item = PostSeriesBlockItem()
    
    class Meta:
        icon = 'lits-ul'
        label = _('Post series ONE')
        
        
class PostSeries2Block(WrapperBlock):
    item = PostSeriesBlockItem()
    
    class Meta:
        label = _('Post series TWO')


class PostSeriesBlock(StructBlock):
    """Block to display contents for post series. E.g. main post
    and its subposts."""
    header = CardHeaderBlock()
    style = CardStyleChoiceBlock(
        required=False,
        label=_('Block style'),
    )
    alignment = TextAlignmentChoiceBlock(
        required=False,
        label=_('Text alignment'),
    )
    post_link_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Post link style'),
    )
    current_post_style = ChoiceBlock(
        required=False,
        choices=[
            ('', 'Default'),
            ('fw-bold', 'Bold'),
            ('fw-bolder', 'Bolder'),
            ('fw-semibold', 'Semibold'),
            ('fw-normal', 'Normal'),
            ('fw-light', 'Light'),
            ('fw-lighter', 'Lighter'),
            ('fst-italic', 'Italic'),
            ('fw-bold fst-italic', 'Bold italic'),
            ('fw-bolder fst-italic', 'Bolder italic'),
            ('fw-semibold fst-italic', 'Semibold italic'),
            ('fw-light fst-italic', 'Light italic'),
            ('fw-lighter fst-italic', 'Lighter italic'),
        ],
        default='',
        label=_('Current post style'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
            if (block.name != 'header'):
                block.field.widget.attrs.update({
                'placeholder': block.label,
            })

    class Meta:
        icon = 'list-ul'
        label = _('Post series')
        form_template = 'waggylabs/blocks/form_template/post_series.html'
        template = 'waggylabs/blocks/template/post_series.html'
        help_text = _('If the post is included into a series, '
                      'its title appears in this block.')