from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, ListBlock, ChoiceBlock, IntegerBlock
)
from wagtail.images.blocks import ImageChooserBlock

from waggylabs.widgets import DisabledOptionSelect

from .markdown import MarkdownBlock


class CarouselItem(StructBlock):
    """Block for the carousel item."""
    image = ImageChooserBlock(
        required=True,
        label=_('Picture for carousel'),
    )
    caption = MarkdownBlock(
        required=False,
        label=_('Text in front of the picture'),
        help_text='',
        easymde_min_height='100px',
        easymde_max_height='100px',
        easymde_combine='true',
        easymde_toolbar_config=('bold,italic,strikethrough,heading,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false',
    )
    interval = IntegerBlock(
        required=False,
        min_value=0,
        label=_('Interval in milliseconds to keep the item'),
        help_text=_('Enter the value in milliseconds to keep the current item '
                    'during this interval'),
        default=1000,
    )
    text_justify = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Text alignment')),
            ('text-start', _('Left')),
            ('text-center', _('Center')),
            ('text-end', _('Right')),
        ],
        default='',
        label=_('Text alignment'),
        widget=DisabledOptionSelect,
    )
    text_color = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Text color')),
            ('text-light', _('Light')),
            ('text-dark', _('Dark')),
        ],
        default='',
        label=_('Text color'),
        widget=DisabledOptionSelect,
    )
    text_size = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Text size')),
            ('fs-6', _('Normal')),
            ('fs-5', _('Bigger')),
            ('fs-4', _('Big')),
            ('fs-3', _('Larger')),
            ('fs-2', _('Large')),
        ],
        default='',
        label=_('Text size'),
        widget=DisabledOptionSelect,
    )
    
    class Meta:
        icon = 'image'
        label = _('Item of the carousel')
        form_template = 'waggylabs/blocks/form_template/carousel_item.html'
        label_format = _('{image}')


class ImageCarouselBlock(StructBlock):
    """Carousel Block with images with possible caption."""
    color = ChoiceBlock(
        choices=[
            ('', _('Color')),
            (' ', _('Light')),
            ('carousel-dark', _('Dark')),
        ],
        default='',
        label=_('Carousel color'),
        widget=DisabledOptionSelect,
    )
    switch = ChoiceBlock(
        choices=[
            ('', _('Switching style')),
            ('false', _('Change on button')),
            ('false-fade', _('Fade on button')),
            ('carousel', _('Change after interval')),
            ('carousel-fade', _('Fade after interval'))
        ],
        default='',
        label=_('Carousel switch type'),
        widget=DisabledOptionSelect,
    )
    controls = ChoiceBlock(
        choices=[
            ('', _('Controls')),
            ('none', _('No controls')),
            ('buttons', _('Left and right buttons')),
            ('indicators', _('Items indicators')),
            ('buttons_indicators', _('Buttons and indicators')),
        ],
        default='',
        label=_('Controls of the carousel'),
        widget=DisabledOptionSelect,
    )
    items = ListBlock(CarouselItem(), min_num=1)
        
    class Meta:
        icon = 'grip'
        label = _('Picture Carousel')
        template = 'waggylabs/blocks/template/carousel.html'
        form_template = 'waggylabs/blocks/form_template/carousel.html'
        label_format = _('Carousel: {items}')