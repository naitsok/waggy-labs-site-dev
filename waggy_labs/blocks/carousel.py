from wagtail.core.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock

from .mathjax_markdown import MathJaxMarkdownBlock


class ImageWithCaptionBlock(StructBlock):
    """Image with caption block for carousel."""
    image = ImageChooserBlock()
    caption = MathJaxMarkdownBlock(
        required=False,
        )