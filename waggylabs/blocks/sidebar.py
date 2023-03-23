
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StreamBlock, StructBlock, ChoiceBlock
)

from waggylabs.blocks.card_header import CardHeaderBlock
from waggylabs.blocks.markdown import MarkdownBlock
from waggylabs.blocks.page_info import PageInfoBlock
from waggylabs.blocks.post_category_list import PostCategoryListBlock
from waggylabs.blocks.post_highlights import PostHighlightsBlock
from waggylabs.blocks.post_series import PostSeriesBlock, PostSeries1Block, PostSeries2Block
from waggylabs.blocks.post_tag_list import PostTagListBlock
from waggylabs.blocks.sidebar_tabs import SidebarTabsBlock
from waggylabs.blocks.styling import CardStyleChoiceBlock


class CitationsBlock(StructBlock):
    """Adds block with references to the side bar. Only one such block can be
    added."""
    header = CardHeaderBlock()
    style = CardStyleChoiceBlock()
    class Meta:
        icon = 'list-ol'
        label = _('References')
        help_text = _('Adds references to the sidebar.')
        template = 'waggylabs/blocks/sidebar_contents.html'
        

class TableOfContentsBlock(StructBlock):
    """Block to add table of contents in the sidebar."""
    header = CardHeaderBlock()
    style = CardStyleChoiceBlock()
    
    class Meta:
        icon = 'list-ul'
        label = _('Table of contents')
        help_text = _('Adds table of contents tab to the sidebar. All the '
                      'headers present on the text blocks of the page body '
                      'will appear as headers in the table of contents.')
        template = 'waggylabs/blocks/template/sidebar_toc.html'
        
class TextBlock(StructBlock):
    """Block to add a simple text piece in the sidebar."""
    header = CardHeaderBlock()
    style = CardStyleChoiceBlock()
    text = MarkdownBlock(
        required=True,
        label=_('Text'),
        help_text=None,
        easymde_min_height='100px',
        easymde_max_height='100px',
        easymde_combine='true',
        easymde_toolbar_config=('bold,italic,strikethrough,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false',
    )
    
    class Meta:
        icon = 'doc-full'
        label = _('Sidebar text')
        help_text = _('Adds text block the sidebar.')
        template = 'waggylabs/blocks/template/sidebar_text.html'
        

class SidebarItemBlock(StreamBlock):
    """Block that contains different sidebar items."""
    text = TextBlock()
    citations = CitationsBlock()
    page_info = PageInfoBlock()
    post_category_list = PostCategoryListBlock()
    post_highlights = PostHighlightsBlock()
    post_series = PostSeriesBlock()
    post_series1 = PostSeries1Block()
    post_series2 = PostSeries2Block()
    post_tag_list = PostTagListBlock()
    tabs = SidebarTabsBlock()
    toc = TableOfContentsBlock()
    
    class Meta:
        icon = 'tasks'
        label = _('Item of the sidebar')
        block_counts = {
            'page_info': { 'max_num': 1 },
            'post_category_list': { 'max_num': 1},
            'post_tag_list': { 'max_num': 1},
            'post_series': { 'max_num': 1 },
            'tabs': { 'max_num': 1 },
        }

class SidebarBlock(StructBlock):
    """A customizable sidebar block."""
    style = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Fixed')),
            ('sticky-top', _('Sticky')),
        ],
        default='',
        label=_('Style of the sidebar'),
    )
    items = SidebarItemBlock()
    
    class Meta:
        icon = 'clipboard-list'
        label = _('Sidebar')
        template = 'waggylabs/blocks/template/sidebar.html'
    