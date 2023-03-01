from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    CharBlock, ChoiceBlock, StructBlock, IntegerBlock,
    BooleanBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import (
    HeaderStyleChoiceBlock, CardStyleChoiceBlock
) 

from waggylabs.widgets import DisabledOptionSelect



class PostListBlock(StructBlock):
    """Block to show posts and their pagination."""
    show_pinned_posts = BooleanBlock(
        required=False,
        label=_('Show pinned posts'),
    )
    pinned_posts_header = CharBlock(
        required=False,
        label=_('Pinned posts header')
    )
    pinned_posts_icon = IconBlock(
        required=False,
        label=_('Pinned posts icon - start typing'),
    )
    pinned_posts_icon_location = IconLocationBlock(required=False)
    pinned_posts_header_style = HeaderStyleChoiceBlock(
        required=False,
        label=_('Pinned posts header style'),
    )
    
    posts_header = CharBlock(
        required=False,
        label=_('Post list header')
    )
    posts_icon = IconBlock(
        required=False,
        label=_('Post list icon - start typing'),
    )
    posts_icon_location = IconLocationBlock(required=False)
    posts_header_style = HeaderStyleChoiceBlock(
        required=False,
        label=_('Post list header style'),
    )
    posts_per_page = IntegerBlock(
        required=True,
        default=5,
        min_value=1,
        label=_('Posts per page'),
    )
    previous_page_text = CharBlock(
        required=False,
        label=_('Previous page text'),
    )
    previous_page_icon = IconBlock(
        required=False,
        label=_('Prev page icon - start typing'),
    )
    next_page_text = CharBlock(
        required=False,
        label=_('Next page text'),
    )
    next_page_icon = IconBlock(
        required=False,
        label=_('Next page icon - start typing'),
    )
    page_alignment = ChoiceBlock(
        required=False,
        choices=[
            ('', 'Paginator alignment'),
            ('justify-content-start', _('Left')),
            ('justify-content-center', _('Center')),
            ('justify-content-end', _('Right')),
        ],
        default='',
        label=_('Paginator alignment'),
        widget=DisabledOptionSelect,
    )
    page_size = ChoiceBlock(
        required=False,
        choices=[
            ('', 'Paginator text size'),
            ('pagination-sm', _('Small')),
            ('pagination-normal', _('Normal')),
            ('pagination-lg', _('Large')),
        ],
        default='',
        label=_('Paginator text size'),
        widget=DisabledOptionSelect,
    )
    post_style = CardStyleChoiceBlock(required=False)
    