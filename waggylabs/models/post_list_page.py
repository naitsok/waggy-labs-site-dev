from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, HelpPanel, MultiFieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.search import index

from wagtailmenus.models import MenuPageMixin
from wagtailmenus.panels import menupage_panel

from waggylabs.blocks.body import BodyBlock
from waggylabs.blocks.sidebar import SidebarBlock
from waggylabs.panels import ReadOnlyPanel

from .base_page import BasePage


class PostListPage(BasePage, MenuPageMixin):
    """Post list page handles preview of posts in a list.
    It includes previewing by date, by category, tags, creator, etc."""
    
    # Common fields
    
    page_description = ('Post page keeps posts content, such as blog posts or '
                        'news posts. It has series functionality to combine posts '
                        'within series of topic-related posts.')
    template = 'waggylabs/pages/post_list_page.html'

    show_in_menus_default = True
    
    # Databse fields
    pin_in_list = models.BooleanField(
        default=False,
        help_text=_('Indicates if the post is pinned on the post list page.'),
        verbose_name=_('Pin in list'),
    )
    
    # Parent page / subpage type rules
    
    parent_page_types = ['wagtail.models.Page', 'waggylabs.SitePage']
    subpage_types = ['waggylabs.PostPage']
    
    # Methods