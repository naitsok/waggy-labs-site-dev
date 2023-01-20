
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, CharBlock, BooleanBlock, StreamBlock
    )


class TableOfContentsBlock(StructBlock):
    """Block to add table of contents in the sidebar."""
    title = CharBlock(
        required=True,
        label=_('Title'),
    )
    
    class Meta:
        icon = ''
        label = _('Table of contents')
        help_text = _('Adds table of contents block in the sidebar.')
        
        
class VisualPreviewBlock(StructBlock):
    """Block to separately in dialog preview figures,
    tables. Equations, embeds, listings are included on request."""
    title = CharBlock(
        required=True,
        label=_('Title'),
    )
    include_embeds = BooleanBlock(
        required=False,
        label=_('Include embeds'),
    )
    include_equations = BooleanBlock(
        required=False,
        label=_('Include equations'),
    )
    include_listings = BooleanBlock(
        required=False,
        label=_('Include listings'),
    )
    
    class Meta:
        icon = ''
        label = _('Visuals')
        help_text = _('Adds thumbnails of visuals (Figures, Tables) '
                      'used in the page body field to the sidebar. The thumbnails '
                      'can be clicked to display the selected visual at full size '
                      'in a dialog box. Listings, embeds, and equations are added according '
                      'to selected settings. There can be several visual blocks '
                      'presenting different visual content.')