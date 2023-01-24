
from django.utils.safestring import mark_safe
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
    
    def render_basic(self, value, context=None):
        return mark_safe('<div class="waggylabs-sidebar-toc"></div>')
    
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
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
    
    def render(self, value, context):
        page = context['page']
        block_types = {
            'embed': value['include_embeds'],
            'equation': value['include_equations'],
            'figure': value['include_figures'],
            'listing': value['include_listings'],
            'table': value['include_tables'],
            'table_figure': value['include_tables'],
        }
        visuals = []
        for block in page.body:
            if block.block_type in block_types and block_types[block.block_type]:
                visuals.append(block)
        value['visuals'] = visuals
        
        return super().render(value, context)
    
    class Meta:
        icon = 'form'
        label = _('Visuals')
        help_text = _('Adds sidebar tab with the selected visuals. More than '
                      'one such sidebar tab can be added with different visuals '
                      'selected. Selected visuals will appear as thumbnails '
                      'in the sidebar and open in a dialog box for the preview.')
        template = 'waggylabs/frontend_blocks/visuals_preview.html'
        
        
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
    
    def render_basic(self, value, context=None):
        return mark_safe('<div class="waggylabs-sidebar-citations"></div>')
    
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
    buttons_style = ChoiceBlock(
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
            ('link-default', _('Default link')),
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
    tabs_font_size = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose font size')),
            ('fs-6', _('Normal')),
            ('fs-5', _('Bigger')),
            ('fs-4', _('Big')),
            ('fs-3', _('Larger')),
            ('fs-2', _('Large')),
        ],
        default='',
        label=_('Tabs font size'),
    )
    tabs_orientation = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose button orientation')),
            ('tabs-default', _('Horizontal')),
            ('flex-column', _('Vertical')),
        ],
        default='',
        label=_('Tabs orientation'),
    )
    tabs_justify = ChoiceBlock(
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
    