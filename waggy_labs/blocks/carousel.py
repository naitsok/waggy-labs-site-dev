from re import template
from wagtail.core.blocks import StructBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock

from .mathjax_markdown import MathJaxMarkdownBlock


class ImageWithCaptionBlock(StructBlock):
    """Image with caption block for carousel."""
    image = ImageChooserBlock()
    caption = MathJaxMarkdownBlock(
        required=False,
        easymde_min_height='150px',
        easymde_max_height='1500px',
        easymde_combine='true',
        easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide'
        )


class ImageCarouselBlock(ListBlock):
    """Carousel Block with images with possible caption."""
    def __init__(self, **kwargs):
        super().__init__(ImageWithCaptionBlock(), **kwargs)
    class Meta:
        icon = 'grip'
        label = 'Image Carousel'
        template = 'waggy_labs/blocks/carousel.html'