from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (
    StructBlock, CharBlock, ListBlock,
    PageChooserBlock, StreamBlock, URLBlock,
    ChoiceBlock
    )
from wagtail.images.blocks import ImageChooserBlock

from .mathjax_markdown import MathJaxMarkdownBlock

class LinksBlock(StreamBlock):
    """Block to add external links and links to Wagtail pages to a card."""
    external_link = StructBlock([
        ('link', URLBlock(
            required=True,
            label=_('Link to external site'),
        )),
        ('text', CharBlock(
            required=True,
            label=_('Text of the link'),
        )),
        ('style', ChoiceBlock(
            choices=[
                ('btn btn-primary', _('Button')),
                ('card-link', _('Link')),
            ],
            default='card-link',
            label=_('Style of link'),
        )),
    ])
    internal_link = StructBlock([
        ('link', PageChooserBlock(
            label=_('Link to this site page'),
        )),
        ('text', CharBlock(
            required=True,
            label=_('Text of the link'),
        )),
        ('style', ChoiceBlock(
            choices=[
                ('btn btn-primary', _('Button')),
                ('card-link', _('Link')),
            ],
            default='card-link',
            label=_('Style of link'),
        )),
    ])
    social_link = StructBlock([
        
    ])
    
    
    class Meta:
        icon = 'link'
        label = _('Card footer links')


class CardBlock(StructBlock):
    """A one card block."""
    image = ImageChooserBlock(required=False)
    title = CharBlock(required=True)
    text = MathJaxMarkdownBlock(required=False)
    links = LinksBlock(required=False)
    
    class Meta:
        icon = 'form'
        label = _('Item of the card grid')
        template = 'waggylabs/blocks/card.html'
        

DEFAULT_CARD_GRID_COLUMNS = 4
DEFAULT_CARD_GRID_COLUMN = 3
class CardGridBlock(StructBlock):
    """Card grid block for StreamField."""
    equal_height = ChoiceBlock(
        choices=[
            ('equal', _('Equal')),
            ('not_equal', _('Wrap content')),
        ],
        default='equal',
        label=_('Height'),
    )
    style = ChoiceBlock(
        choices=[
            ('separate', _('Separate')),
            ('grouped', _('Grouped')),
        ],
        default='separate',
        label=_('Grouping'),
    )
    orientation = ChoiceBlock(
        choices=[
            ('vertical', _('Vertical')),
            ('horizontal', _('Horizontal')),
        ],
        default='vertical',
        label=_('Orientation'),
    )
    columns = ChoiceBlock(
        choices=[
            (i + 1, i + 1) for i in 
            range((settings.WAGGYLABS_CARD_GRID_COLUMNS if 
                   hasattr(settings, 'WAGGYLABS_CARD_GRID_COLUMNS') 
                   else DEFAULT_CARD_GRID_COLUMNS))
        ],
        default=(settings.WAGGYLABS_CARD_GRID_COLUMN if 
                 hasattr(settings, 'WAGGYLABS_CARD_GRID_COLUMN') 
                 else DEFAULT_CARD_GRID_COLUMN),
        label=_('Number of columns'),
    )
    cards = ListBlock(CardBlock())
    
