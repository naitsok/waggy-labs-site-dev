from django.apps import apps
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    ChoiceBlock, StructBlock, CharBlock, PageChooserBlock,
    BooleanBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import (
    CardStyleChoiceBlock, HeaderStyleChoiceBlock
)
from waggylabs.models.post_category import PostCategory, PostPagePostCategory


class PostCategoryListBlock(StructBlock):
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
    categories_style = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Default')),
            ('list-group-flush', _('No outer borders')),
            ('list-group-numbered', _('Numbers before category')),
            ('list-group-numbered list-group-flush', _('Numbers and no outer border')),
        ],
        default='',
        label=_('Categories style'),
    )
    category_style = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Default')),
            ('list-group-item-primary', _('Primary')),
            ('list-group-item-secondary', _('Secondary')),
            ('list-group-item-success', _('Success')),
            ('list-group-item-danger', _('Danger')),
            ('list-group-item-warning', _('Warning')),
            ('list-group-item-info', _('Info')),
            ('list-group-item-light', _('Light')),
            ('list-group-item-dark', _('Dark')),
        ],
        default='',
        label=_('Category item style'),
    )
    order_by = ChoiceBlock(
        required=False,
        choices=[
            ('created_at', _('Older first')),
            ('-created_at', _('Newer first')),
            ('slug', _('By slug acsending')),
            ('-slug', _('By slug descending')),
            ('num_posts', _('By post number acsending')),
            ('-num_posts', _('By post number descending')),
        ],
        default='created_at',
        label=_('Categories ordering'),
    )
    show_badges = BooleanBlock(
        required=False,
        label=_('Show number of posts per category'),
        
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
        category_query =  None
        if not value['post_list_page'] and \
            context['page'].specific_class.__name__ == 'PostListPage':
            value['post_list_page'] = context['page']
            
        if value['post_list_page']:
            category_query = PostCategory.objects.filter(
                id__in=PostPagePostCategory.objects.filter(
                    post_page__in=post_page_model.objects.descendant_of(value['post_list_page']).live()
                ).values('post_category__id').distinct())

            if value['show_badges']:
                category_query = category_query.annotate(num_posts=Count('post_pages'))
        
            if not value['order_by']:
                value['order_by'] = '-created_at'
            
            category_query = category_query.order_by(value['order_by'])
        value['categories'] = category_query
        return super().render(value, context)
        
    class Meta:
        icon = 'list-ul'
        label = _('Post categories')
        template = 'waggylabs/blocks/template/post_category_list.html'
        form_template = 'waggylabs/blocks/form_template/post_category_list.html'