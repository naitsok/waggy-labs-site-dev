
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, CharBlock, BooleanBlock, StreamBlock,
    ChoiceBlock
    )

from waggylabs.blocks.icon import IconBlock
from waggylabs.widgets import DisabledOptionSelect

class TableOfContentsBlock(StructBlock):
    """Block to add table of contents in the sidebar."""
    title = CharBlock(
        required=False,
        label=_('Title'),
        help_text=_('Title to appear on the tab.'),
    )
    icon = IconBlock(
        required=False,
        label=_('Icon'),
    )
    
    class Meta:
        icon = 'list-ul'
        label = _('Table of contents')
        help_text = _('Adds table of contents tab to the sidebar.') 
 
        
class VisualPreviewBlock(StructBlock):
    """Block to add thumbnails on visuals to sidebar.
    Embeds, equations, """
    title = CharBlock(
        required=False,
        label=_('Title'),
        help_text=_('Title to appear on the tab.'),
    )
    icon = IconBlock(
        required=False,
        label=_('Icon'),
    )
    include_embeds = BooleanBlock(
        required=False,
        label=_('Include embeds'),
    )
    include_equations = BooleanBlock(
        required=False,
        label=_('Include equations'),
    )
    include_figures = BooleanBlock(
        required=False,
        label=_('Include figures'),
    )
    include_listings = BooleanBlock(
        required=False,
        label=_('Include listings'),
    )
    include_tables = BooleanBlock(
        required=False,
        label=_('Include tables'),
    )
    
    class Meta:
        icon = 'form'
        label = _('Visuals')
        help_text = _('Adds sidebar tab with the selected visuals. More than '
                      'one such sidebar tab can be added with different visuals '
                      'selected. Selected visuals will appear as thumbnails '
                      'in the sidebar and open in a dialog box for the preview.')
        
        
class CitationsBlock(StructBlock):
    """Adds block with references to the side bar. Only one such block can be
    added."""
    title = CharBlock(
        required=False,
        label=_('Title'),
        help_text=_('Title to appear on the tab.'),
    )
    icon = IconBlock(
        required=False,
        label=_('Icon'),
    )
    
    class Meta:
        icon = 'list-ol'
        label = _('References')
        help_text = _('Adds references to the sidebar.')
        
        
class SidebarTabsBlock(StreamBlock):
    """Block to add tabs to sidebar with different content."""
    table_of_contents = TableOfContentsBlock()
    visuals = VisualPreviewBlock()
    citations = CitationsBlock()
    
    class Meta:
        icon = 'clipboard-list'
        label = _('Sidebar')
        block_counts = {
            'table_of_contents': {'max_num': 1},
            'citations': {'max_num': 1},
        }

        
class SidebarBlock(StructBlock):
    """Sidebar block for the the page."""
    tabs_style = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose tabs style')),
            ('nav nav-tabs', _('Tabs')),
            ('nav nav-pills', _('Pills')),
            ('nav nav-pills nav-fill', _('Wide pills')),
        ],
        default='',
        label=_('Tabs style'),
    )
    tab_buttons_style = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose button style')),
            ('btn btn-primary', _('Button primary')),
            ('btn btn-secondary', _('Button secondary')),
            ('btn btn-success', _('Button success')),
            ('btn btn-danger', _('Button danger')),
            ('btn btn-warning', _('Button warning')),
            ('btn btn-info', _('Button info')),
            ('btn btn-outline-primary', _('Button outline primary')),
            ('btn btn-outline-secondary', _('Button outline secondary')),
            ('btn btn-outline-success', _('Button outline success')),
            ('btn btn-outline-danger', _('Button outline danger')),
            ('btn btn-outline-warning', _('Button outline warning')),
            ('btn btn-outline-info', _('Button outline info')),
            ('nav-link', _('Navigation bar link')),
            ('link-primary', _('Primary link')),
            ('link-secondary', _('Secondary link')),
            ('link-success', _('Success link')),
            ('link-danger', _('Danger link')),
            ('link-warning', _('Warning link')),
            ('link-info', _('Info link')),
            ('link-light', _('Light link')),
            ('link-dark', _('Dark link')),
        ],
        default='',
        label=_('Tab buttons style'),
    )
    tab_buttons_orientation = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose button orientation')),
            ('horizontal', _('Horizontal')),
            ('vertical', _('Vertical')),
        ],
        default='',
        label=_('Tabs orientation'),
    )
    tab_buttons_justify = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose horizontal alignment')),
            ('justify-content-start', _('Align left')),
            ('justify-content-center', _('Align center')),
            ('justify-content-end', _('Align right')),
        ],
        default='',
        label=_('Tabs orientation'),
    )
    
    items = SidebarTabsBlock()
    
    class Meta:
        icon = 'clipboard-list'
        label = _('Sidebar')
        template = 'waggylabs/frontend_blocks/sidebar.html'
        form_template = 'waggylabs/blocks/sidebar.html'
        label_format = _('Sidebar: {items}')
        help_text = _('Choose the style of the sidebar and which panels to use. '
                      'Note that some settings are incompartible. If tabs style is '
                      '"Tabs", then only link styles will be used for titles. '
                      'Vertical orientation of tab buttons does not support "Tabs" '
                      'style.')
    