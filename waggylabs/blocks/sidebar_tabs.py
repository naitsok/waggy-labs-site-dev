
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, CharBlock, BooleanBlock, StreamBlock,
    ChoiceBlock
    )

from waggylabs.blocks.base_body import BaseBodyBlock
from waggylabs.blocks.card_header import CardHeaderBlock
from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.post_series import PostSeriesBlock
from waggylabs.blocks.styling import (
    LinkStyleChoiceBlock, CardStyleChoiceBlock, HeaderStyleChoiceBlock
)


class TabHeaderBlock(StructBlock):
    """Block for tab title, icon, icon location."""
    title = CharBlock(
        required=False,
        label=_('Tab title'),
        help_text=_('Title to appear on the tab.'),
    )
    icon = IconBlock(
        required=False,
        label=_('Tab icon'),
    )
    icon_location = IconLocationBlock(
        required=False,
        label=_('Tab icon location'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
            block.field.widget.attrs.update({
                'placeholder': block.label,
            })
    
    class Meta:
        form_template = 'waggylabs/blocks/form_template/sidebar_tab_header.html'
        label = _('Tab header')

class PostSeriesTabBlock(StructBlock):
    """Tab to display series contents."""
    tab_header = TabHeaderBlock(
        help_text=_('Post series block style, header, header will be ignored '
                      'when the tab is rendered.')
    )
    item = PostSeriesBlock()
    
    class Meta:
        icon = 'list-ul'
        label = _('Post series')
        # help_text = _('Post series block style, header, header will be ignored '
        #               'when the tab is rendered.')
        template = 'waggylabs/blocks/template/sidebar_tab_wrapper.html'
    


class TableOfContentsTabBlock(StructBlock):
    """Block to add table of contents in the sidebar."""
    tab_header = TabHeaderBlock()
    
    def render_basic(self, value, context=None):
        return mark_safe('<div class="waggylabs-sidebar-toc text-wrap"></div><hr>')
    
    class Meta:
        icon = 'list-ul'
        label = _('Table of contents')
        help_text = _('Adds table of contents tab to the sidebar. All the '
                      'headers present on the text blocks of the page body '
                      'will appear as headers in the table of contents.')
 
        
class VisualsBlock(StructBlock):
    """Block to add thumbnails on visuals to sidebar.
    Embeds, equations, figures, listings, tables can be included."""
    header = TabHeaderBlock()
    style = CardStyleChoiceBlock()
    preview_buttons_text = CharBlock(
        required=False,
        label=_('Preview buttons text'),
        
    )
    preview_buttons_icon = IconBlock(
        required=False,
        label=_('Preview buttons icon'),
    )
    preview_buttons_icon_location = IconLocationBlock(
        required=False,
        label=_('Preview buttons icon location'),
    )
    preview_buttons_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Preview buttons style'),
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
        self.child_blocks['preview_buttons_text'].field.widget.attrs.update({
            'placeholder': _('Preview button text'),
        })
    
    def render(self, value, context):
        block_types = []
        for key, val in value.items():
            if 'include_' in key and val:
                block_types.append(key[8:-1])
        if value['include_tables']:
            block_types.append('table_figure')
        
        value['visuals'] = BaseBodyBlock.blocks_by_types(
            context['page'].body,
            block_types
        )
        
        return super().render(value, context)
    
    class Meta:
        icon = 'image'
        label = _('Visuals')
        help_text = _('Adds sidebar block with the selected visuals. More than '
                      'one such block can be added with different visuals '
                      'selected. Selected visuals will appear as thumbnails '
                      'in the sidebar and open in a dialog box for the preview.')
        template = 'waggylabs/blocks/template/visuals.html'
        form_template = 'waggylabs/blocks/form_template/visuals.html'
        
        
class CitationsTabBlock(StructBlock):
    """Adds block with references to the side bar. Only one such block can be
    added."""
    tab_header = TabHeaderBlock()
    
    def render_basic(self, value, context=None):
        return mark_safe('<div class="waggylabs-sidebar-literature"></div>')
    
    class Meta:
        icon = 'list-ol'
        label = _('References')
        help_text = _('Adds references to the sidebar.')
        
        
class SidebarTabItemBlock(StreamBlock):
    """Block to add tabs to sidebar with different content."""
    table_of_contents = TableOfContentsTabBlock()
    visuals = VisualsBlock()
    citations = CitationsTabBlock()
    post_series = PostSeriesTabBlock()
    
    class Meta:
        icon = 'clipboard-list'
        label = _('Sidebar tabs')
        block_counts = {
            'table_of_contents': { 'max_num': 1 },
            'citations': { 'max_num': 1 },
            'post_series': { 'max_num': 1 },
        }

        
class SidebarTabsBlock(StructBlock):
    """Sidebar block with tabs for the the page. Tabs can contain
    contents (generated from headers on page), page visuals"""
    style = CardStyleChoiceBlock(
        required=False,
        label=_('Block style'),
    )
    header = CharBlock(
        required=False,
        label=_('Header: e.g. "Next post"'),
    )
    header_style = HeaderStyleChoiceBlock(
        required=False,
        label=_('Header style'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('Header icon'),
    )
    header_icon_location = IconLocationBlock(
        required=False,
        label=_('Header icon location'),
    )
    tabs_style = ChoiceBlock(
        required=False,
        choices=[
            ('nav nav-tabs', _('Tabs')),
            ('nav nav-pills', _('Pills')),
            ('nav nav-pills nav-fill', _('Wide pills')),
        ],
        default='nav nav-tabs',
        label=_('Tabs style'),
    )
    buttons_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Tab buttons style'),
    )
    tabs_font_size = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Default')),
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
        required=False,
        choices=[
            ('', _('Horizontal')),
            ('flex-column', _('Vertical')),
        ],
        default='',
        label=_('Tabs orientation'),
    )
    tabs_justify = ChoiceBlock(
        required=True,
        choices=[
            ('justify-content-start', _('Align left')),
            ('justify-content-center', _('Align center')),
            ('justify-content-end', _('Align right')),
        ],
        default='justify-content-start',
        label=_('Tabs horizontal alignment'),
    )
    # tabs_close = BooleanBlock(
    #     required=False,
    #     label=_('Show close button'),
    #     help_text=_('Allows to collapse sidebar and use full page with for content.'),
    # )
    
    
    items = SidebarTabItemBlock()
    
    class Meta:
        icon = 'clipboard-list'
        label = _('Sidebar tabs')
        template = 'waggylabs/blocks/template/sidebar_tabs.html'
        form_template = 'waggylabs/blocks/form_template/sidebar_tabs.html'
        label_format = _('Sidebar: {items}')
        help_text = _('Choose the style of the sidebar and which panels to use. '
                      'Note that some settings are incompartible. If tabs style is '
                      '"Tabs", then only link styles will be used for titles. '
                      'Vertical orientation of tab buttons does not support "Tabs" '
                      'style. When blocks are rendered within tabs, their header '
                      'text and icon becomes the tab header and icon, while the '
                      'header style is ignored.')
    