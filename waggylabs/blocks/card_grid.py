from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (
    StructBlock, CharBlock, ListBlock,
    PageChooserBlock, StreamBlock, URLBlock
    )
from wagtail.images.blocks import ImageChooserBlock

from .mathjax_markdown import MathJaxMarkdownBlock

class LinksBlock(StreamBlock):
    """Block to add external links and links to Wagtail pages to a card."""
    external_link = URLBlock(
        required=True,
        label=_('Link to external site'),
        )
    internal_link = PageChooserBlock(
        label=_('Link to this site page'),
    )
    
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
