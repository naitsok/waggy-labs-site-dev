from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from wagtailmarkdown.utils import render_markdown

from waggylabs.fields import MarkdownField


@register_snippet
class PostCategory(models.Model):
    """Class for post categories."""

    # Database fields

    name = MarkdownField(blank=False)
    slug = models.SlugField(unique=True, max_length=255, blank=False)

    # Editor panels configuration

    panels = [
        FieldPanel('name'),
        FieldPanel('slug', classname='full'),
        ]

    def __str__(self):
        return render_markdown(self.name)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class PostPagePostCategory(models.Model):
    """A connection class for inline panel to work."""
    post_page = ParentalKey(
        'waggylabs.PostPage',
        on_delete=models.CASCADE,
        related_name='post_categories',
    )
    post_category = models.ForeignKey(
        'waggylabs.PostCategory',
        on_delete=models.CASCADE,
        related_name='post_pages',
    )

    panels = [
        FieldPanel('post_category'),
    ]

    class Meta:
        unique_together = ('post_page', 'post_category')