from django.apps import apps
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    ChoiceBlock, StructBlock, CharBlock, PageChooserBlock,
    BooleanBlock, IntegerBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import (
    CardStyleChoiceBlock, HeaderStyleChoiceBlock, LinkStyleChoiceBlock
)
from waggylabs.models.post_tags import PostPageTag
# from waggylabs.models.post_page import PostPage


class PostTagListBlock(StructBlock):
    """Block to show post categories."""
    post_list_page = PageChooserBlock(
        required=False,
        page_type='waggylabs.PostListPage',
        label=_('Root post list page'),
        help_text=_('Shows post categories for the posts, which are '
                    'children of the selected post list page. '
                    'If left empty, the currently browsed post list page will '
                    'be used, or all categories will be displayed if the '
                    ' currently browsed page is not a post lit page.'),
    )
    block_style = CardStyleChoiceBlock(
        required=False,
        label=_('Block style'),
    )
    header = CharBlock(
        required=False,
        label=_('Header'),
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
    tags_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Tags style'),
    )
    tags_number = IntegerBlock(
        required=True,
        default=10,
        min_value=0,
        label=_('Number of the most popular tags to show'),
        help_text=_('If equals to zero, then all tags '
                    'are shown.')
    )
    order_by = ChoiceBlock(
        required=False,
        choices=[
            ('slug', _('By slug acsending')),
            ('-slug', _('By slug descending')),
            ('num_posts', _('By post number acsending')),
            ('-num_posts', _('By post number descending')),
        ],
        default='slug',
        label=_('Tags ordering'),
    )
    show_badges = BooleanBlock(
        required=False,
        label=_('Show number of posts per tag'),
        
    )
    badge_style = ChoiceBlock(
        required=False,
        choices=[
            ('text-bg-primary', _('Primary')),
            ('text-bg-secondary', _('Secondary')),
            ('text-bg-success', _('Success')),
            ('text-bg-danger', _('Danger')),
            ('text-bg-warning', _('Warning')),
            ('text-bg-info', _('Info')),
            ('text-bg-light', _('Light')),
            ('text-bg-dark', _('Dark')),
            ('rounded-pill text-bg-primary', _('Rounded primary')),
            ('rounded-pill text-bg-secondary', _('Rounded secondary')),
            ('rounded-pill text-bg-success', _('Rounded success')),
            ('rounded-pill text-bg-danger', _('Rounded danger')),
            ('rounded-pill text-bg-warning', _('Rounded warning')),
            ('rounded-pill text-bg-info', _('Rounded info')),
            ('rounded-pill text-bg-light', _('Rounded light')),
            ('rounded-pill text-bg-dark', _('Rounded dark')),
        ],
        default='text-bg-primary',
        label=_('Post number style'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['header'].field.widget.attrs.update({
            'placeholder': self.child_blocks['header'].label,
        })
        
    def render(self, value, context):
        # needed to avoid circular imports
        post_page_model = apps.get_model('waggylabs', 'PostPage')
        tag_query =  None
        if not value['post_list_page'] and \
            context['page'].specific_class.__name__ == 'PostListPage':
            value['post_list_page'] = context['page']
            
        if value['post_list_page']:
            tag_query = PostPageTag.objects.filter(
                content_object_id__in=post_page_model.objects.descendant_of(value['post_list_page']).live()
                ).values('tag__slug').distinct()

            if value['show_badges']:
                tag_query = tag_query.annotate(num_posts=Count('post_pages'))
        
            if not value['order_by']:
                value['order_by'] = '-created_at'
            
            tag_query = tag_query.order_by(value['order_by'])
        value['tags'] = tag_query
        return super().render(value, context)
        
    class Meta:
        icon = 'list-ul'
        label = _('Post categories')
        template = 'waggylabs/blocks/template/post_tag_list.html'
        form_template = 'waggylabs/blocks/form_template/post_tag_list.html'