from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin import widgets
from wagtail.admin.panels import FieldPanel, HelpPanel, MultiFieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.search import index

from hitcount.models import HitCountMixin, HitCount
from hitcount.views import HitCountMixin as ViewHitCountMixin

from waggylabs.blocks.body import BodyBlock
from waggylabs.blocks.sidebar import SidebarBlock
from waggylabs.panels import ReadOnlyPanel

from .base_page import BasePage


class PostPage(BasePage, HitCountMixin):
    """Post page keeps posts content, such as blog posts or
    news posts. It has series functionality to combine posts
    within series of topic-related posts."""
    
    page_description = ('Post page keeps posts content, such as blog posts or '
                        'news posts. It has series functionality to combine posts '
                        'within series of topic-related posts.')
    template = 'waggylabs/pages/post_page.html'
    
    # Parent page / subpage type rules
    
    parent_page_types = ['waggylabs.PostsListPage']
    subpage_types = ['waggylabs.PostPage']
    
    # Methods
    
    @classmethod
    def can_create_at(cls, parent):
        """If the specific class of the parent page is PostPage,
        the hierarchy of the newly added post will be:
        PostPage -> PostPage -> new PostPage. This is too deep 
        heararchy. Series of posts allows only one time ancestor 
        for a PostPage in series."""
        if parent.get_parent().specific_class == PostPage:
            return False
        return super().can_create_at(parent)
    
    @classmethod
    def can_exist_under(cls, parent):
        """Same as PostPage.can_creat_at(parent) classmethod."""
        if parent.get_parent().specific_class == PostPage:
            return False
        return super().can_exist_under(parent)
    
    def can_move_to(self, parent):
        """Same as PostPage.can_creat_at(parent) classmethod."""
        if parent.get_parent().specific_class == PostPage:
            return False
        return super().can_move_to(parent)
    
    def is_series(self):
        """Verifies that post is in the series of topic-related posts."""
        # parent_page = self.get_parent().specific
        if self.get_parent().specific_class == PostPage:
            # this is the child post of series
            return True
        if self.get_children_count() > 0:
            # this is parent post of series
            return True
        return False
    
    def post_series(self):
        """Gets post series for the current post."""
        parent = self.get_parent()
        if parent.specific_class == PostPage:
            return parent.get_descendants(inclusive=True).live().order_by('first_published_at')
        if self.get_children_count() > 0:
            return self.get_descendants(inclusive=True).live().order_by('first_published_at')
        return []
    
    def sibling_posts(self):
        """Returns previous and next posts for the current post.
        Previous means either previously (chronologically) published or 
        previous post from the series. Next means either (chronologically) 
        published next or next post from the series."""
        series = self.post_series()
        if series:
            series_len = series.count()
            for post, idx in enumerate(series):
                if self.pk == post.pk:
                    if idx == 0:
                        return {
                            'previous_post': PostPage.objects.live().filter(
                                    first_published_at__lt=self.first_published_at
                                ).order_by('-first_published_at').first(),
                            'next_post': series[idx + 1],
                        }
                    if idx == series_len - 1:
                        return {
                            'previous_post': series[idx - 1],
                            'next_post': PostPage.objects.live().filter(
                                    first_published_at__gt=self.first_published_at
                                ).order_by('first_published_at').first(),
                        }
                    return {
                        'previous_post': series[idx - 1],
                        'next_post': series[idx + 1],
                    }
        return {
            'previous_post': PostPage.objects.live().filter(
                    first_published_at__lt=self.first_published_at
                ).order_by('-first_published_at').first(),
            'next_post': PostPage.objects.live().filter(
                    first_published_at__gt=self.first_published_at
                ).order_by('first_published_at').first(),
        }