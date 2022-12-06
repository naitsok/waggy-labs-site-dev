from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import StructBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock

from .mathjax_markdown import MathJaxMarkdownBlock


class ImageWithCaptionBlock(StructBlock):
    """Image with caption block for carousel."""
    image = ImageChooserBlock(
        required=True,
        label=_('Picture for carousel'),
    )
    caption = MathJaxMarkdownBlock(
        required=False,
        label=_('Text in front of the picture'),
        help_text='',
        easymde_min_height='100px',
        easymde_max_height='100px',
        easymde_combine='true',
        easymde_toolbar_config=('bold,italic,strikethrough,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false',
    )
    
    class Meta:
        icon = 'image'
        label = _('Item of the carousel')
        label_format = _('{image}')


class ImageCarouselBlock(StructBlock):
    """Carousel Block with images with possible caption."""
    images = ListBlock(ImageWithCaptionBlock(), min_num=1)
        
    class Meta:
        icon = 'grip'
        label = _('Picture Carousel')
        template = 'waggylabs/frontend_blocks/carousel.html'
        form_template = 'waggylabs/blocks/carousel.html'
        label_format = _('Carousel: {images}')