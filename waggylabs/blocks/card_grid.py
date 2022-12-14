from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, CharBlock, ListBlock,
    StreamBlock, ChoiceBlock
)
from wagtail.images.blocks import ImageChooserBlock

from waggylabs.widgets import DisabledOptionSelect

from .links import (
    ExternalLinkBlock, InternalLinkBlock, IconEmailBlock,
    InfoTextBlock
)
from .mathjax_markdown import MathJaxMarkdownBlock


class LinksBlock(StreamBlock):
    """Block to add different links."""
    external_link = ExternalLinkBlock()
    internal_link = InternalLinkBlock()
    email = IconEmailBlock()
    info_text = InfoTextBlock()
    
    class Meta:
        icon = 'link'
        label = _('Links for the card')

class CardBlock(StructBlock):
    """A one card block."""
    image = ImageChooserBlock(required=False, label=_('Image'))
    title = CharBlock(required=True, label=_('Title'))
    subtitle = CharBlock(required=False, label=_('Subtitle'))
    text = MathJaxMarkdownBlock(
        required=False,
        help_text=None,
        easymde_min_height='100px',
        easymde_max_height='100px',
        easymde_combine='true',
        easymde_toolbar_config=('bold,italic,strikethrough,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false',)
    links = LinksBlock(required=False)
    
    class Meta:
        icon = 'form'
        label = _('Item of the card grid')
        template = 'waggylabs/frontend_blocks/card.html'
        label_format = _('{title}')
        

DEFAULT_CARD_GRID_COLUMNS = 5
class CardGridBlock(StructBlock):
    """Card grid block for StreamField."""
    height_style = ChoiceBlock(
        choices=[
            ('', _('Choose height style')),
            ('equal', _('Equal height')),
            ('not_equal', _('Height wraps to content')),
        ],
        default='',
        label=_('Height'),
        widget=DisabledOptionSelect,
    )
    grouping_style = ChoiceBlock(
        choices=[
            ('', _('Choose grouping style')),
            ('separate', _('Separate')),
            ('grouped', _('Grouped')),
        ],
        default='',
        label=_('Grouping'),
        widget=DisabledOptionSelect,
    )
    orientation_style = ChoiceBlock(
        choices=[
            ('', _('Choose orientation')),
            ('vertical', _('Vertical')),
            ('horizontal', _('Horizontal')),
        ],
        default='',
        label=_('Orientation'),
        widget=DisabledOptionSelect,
    )
    columns = ChoiceBlock(
        choices=[
            ('', _('Choose columns')),
            (1, _('1 column')),
        ] + [
            (i + 1, str(i + 1) + _(' columns')) for i in
            range(1, (settings.WAGGYLABS_CARD_GRID_COLUMNS if
                      hasattr(settings, 'WAGGYLABS_CARD_GRID_COLUMNS')
                      else DEFAULT_CARD_GRID_COLUMNS))
        ],
        default='',
        label=_('Number of columns'),
    )
    cards = ListBlock(CardBlock())
    
    class Meta:
        icon = 'form'
        label = _('Card grid')
        template = 'waggylabs/frontend_blocks/card_grid.html'
        form_template = 'waggylabs/blocks/card_grid.html'
        label_format = _('Card grid: {cards}')
