from django.db import models
from django.http import Http404, HttpResponse
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, HelpPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.search import index

from wagtailmenus.models import MenuPageMixin
from wagtailmenus.panels import menupage_panel

from waggylabs.blocks.body import BodyBlock
from waggylabs.blocks.sidebar import SidebarBlock
from waggylabs.panels import ReadOnlyPanel

from .base_page import BasePage
from .post_page import PostPage


class PostListPage(RoutablePageMixin, BasePage, MenuPageMixin):
    """Post list page handles preview of posts in a list.
    It includes previewing by date, by category, tags, creator, etc."""
    
    # Common fields
    
    page_description = ('This is the main page that rules all the posts and post '
                        'routing. All the post pages are children of the post page. '
                        'Give a good slug name of this page, such as "news" or "blog". '
                        'All the posts then will appear with /news/post-slug url.')
    template = 'waggylabs/pages/post_list_page.html'

    show_in_menus_default = True
    
    # Databse fields
    
    # Parent page / subpage type rules
    
    parent_page_types = ['wagtailcore.Page', 'waggylabs.SitePage']
    subpage_types = ['waggylabs.PostPage']
    
    # Methods
    
    def __init__(self):
        super().__init__()
        self.slug.help_text = _(
            'Give this page a well-recognized slug (news, blog, etc.), since '
            'it will be in the url for all the children post pages. For example, '
            'the final url will be https://domain.com/news/post-page, if '
            '"news" was added as slug. If this page is selected as root page of the '
            'site, the slug will be skipped in the url.'
        )
        
    @re_path(r'^(\d{4})-(\d{2})-(\d{2})/(.+)/$')
    @re_path(r'^(\d{4})-(jan?|feb?|mar?|apr?|may?|jun?|jul?|aug?|sep?|oct?|nov?|dec?)-(\d{2})/(.+)/$')
    def post_by_slug(self, request, year, month, date, slug, *args, **kwargs):
        post = PostPage.objects.live().filter(slug=slug).first()
        if post:
            return post.serve(request, *args, **kwargs)
        raise Http404