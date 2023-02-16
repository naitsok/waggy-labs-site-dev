
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StreamBlock, StructBlock, BooleanBlock, ChoiceBlock, CharBlock
)

from waggylabs.blocks.markdown import MarkdownBlock
from waggylabs.blocks.page_info import PageInfoBlock
from waggylabs.blocks.sidebar_tabs import SidebarTabsBlock
from waggylabs.widgets import DisabledOptionSelect


class SidebarItemBlock(StreamBlock):
    """Block that contains different sidebar items."""
    text = MarkdownBlock(
        required=True,
        label=_('Sidebar text'),
        help_text=None,
        easymde_min_height='100px',
        easymde_max_height='100px',
        easymde_combine='true',
        easymde_toolbar_config=('bold,italic,strikethrough,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false',
    )
    page_info = PageInfoBlock()
    tabs = SidebarTabsBlock()
    
    class Meta:
        icon = 'tasks'
        label = _('Item of the sidebar')
        block_counts = {
            'page_info': {'max_num': 1},
            'tabs': {'max_num': 1},
        }

class SidebarBlock(StructBlock):
    """A customizable sidebar block."""
    style = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose sidebar style')),
            ('default', _('Default')),
            ('sticky-top', _('Sticky')),
        ],
        label=_('Style of the sidebar'),
        widget=DisabledOptionSelect,
    )
    items = SidebarItemBlock()
    
    class Meta:
        icon = 'clipboard-list'
        label = _('Sidebar')
        template = 'waggylabs/blocks/template/sidebar.html'
    