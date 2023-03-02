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
        label=_('Pinned posts header'),
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
        label=_('Post list header'),
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
        min_value=1,
        label=_('Posts per page'),
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
    post_style = CardStyleChoiceBlock(
        required=False,
        label=_('Post style in the list'),
    )
    post_title_style = HeaderStyleChoiceBlock(
        required=False,
        label=_('Post title style'),
    )
    show_username = BooleanBlock(
        required=False,
        label=_('Show username'),
    )
    show_avatar = BooleanBlock(
        required=False,
        label=_('Show avatar'),
    )
    show_first_published_at = BooleanBlock(
        required=False,
        label=_('Date of page publication'),
    )
    show_time = BooleanBlock(
        required=False,
        label=_('Show time in the date fields'),
    )
    datetime_style = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Date style')),
            ('date', _('Only date')),
            ('datetime', _('Date and time')),
            ('timesince', _('Time since')),
        ],
        default='',
        label=_('Date style'),
        widget=DisabledOptionSelect,
    )
    time_format = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Time format')),
            ('G:i', _('24-hour format')),
            ('g:i A', _('12-hour format')),
        ],
        label=_('Time format'),
        widget=DisabledOptionSelect,
    )
    timesince_text = CharBlock(
        required=False,
        label=_('Time since text, e.g. ago'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
            block.field.widget.attrs.update({
                'placeholder': block.label,
            })
            
    def render(self, value, context):
        page = context['page']
        value['pinned_posts'] = page.get_descendants(inclusive=False).live()\
            .filter(pin_in_list=True).order_by('-first_published_at')
        value['posts'] = page.get_descendants(inclusive=False).live()\
            .filter(pin_in_list=False).order_by('-first_published_at')
        return super().render(value, context)
    
    class Meta:
        icon = 'list'
        label = _('Post list')
        template = 'waggylabs/blocks/template/post_list.html'
        form_template = 'waggylabs/blocks/form_template/post_list.html'
        help_text = _('Post list block controls the appearence list of posts '
                      'on the page. It can include pinned posts that always appear '
                      'on the first page of page list. Number of post per page, '
                      'their appearance in the list, paginator styles can be alo set.')
    