from django.apps import apps
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    ChoiceBlock, StructBlock, CharBlock, PageChooserBlock,
    BooleanBlock, IntegerBlock
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
                    'be used. Otherwise, no categories will be displayed.'),
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
            ('', _('Default list')),
            ('list-unstyled', _('Unstyled list')),
            ('list-numbered', _('Numbered list')),
            ('list-group', _('List group')),
            ('list-group list-group-flush', _('List group, no outer borders')),
            ('list-group list-group-numbered', _('Numbered list group')),
            ('list-group list-group-numbered list-group-flush', _('Numbered list group, no outer borders')),
        ],
        default='',
        label=_('Categories style'),
    )
    categories_number = IntegerBlock(
        required=True,
        default=10,
        min_value=0,
        label=_('Number of categories to show'),
        help_text=_('Depends on the selected order. '
                    'If equals to zero, then all categories are shown.'),
    )
    category_style = ChoiceBlock(
        required=False,
        choices=[
            ('list-group-item list-group-item-action', _('List group default')),
            ('list-group-item list-group-item-action list-group-item-primary', _('List group primary')),
            ('list-group-item list-group-item-action list-group-item-secondary', _('List group secondary')),
            ('list-group-item list-group-item-action list-group-item-success', _('List group success')),
            ('list-group-item list-group-item-action list-group-item-danger', _('List group danger')),
            ('list-group-item list-group-item-action list-group-item-warning', _('List group warning')),
            ('list-group-item list-group-item-action list-group-item-info', _('List group info')),
            ('list-group-item list-group-item-action list-group-item-light', _('List group light')),
            ('list-group-item list-group-item-action list-group-item-dark', _('List group dark')),
            ('btn btn-primary', _('Button primary')),
            ('btn btn-secondary', _('Button secondary')),
            ('btn btn-success', _('Button success')),
            ('btn btn-danger', _('Button danger')),
            ('btn btn-warning', _('Button warning')),
            ('btn btn-info', _('Button info')),
            ('btn btn-outline-primary', _('Button outline primary')),
            ('btn btn-outline-secondary', _('Button outline secondary')),
            ('btn btn-outline-success', _('Button outline success')),
            ('btn btn-outline-danger', _('Button outline danger')),
            ('btn btn-outline-warning', _('Button outline warning')),
            ('btn btn-outline-info', _('Button outline info')),
            ('card-link', _('Card link')),
            ('nav-link', _('Navigation bar link')),
            ('nav-link active', _('Navigation bar active link')),
            ('link-primary', _('Primary link')),
            ('link-secondary', _('Secondary link')),
            ('link-success', _('Success link')),
            ('link-danger', _('Danger link')),
            ('link-warning', _('Warning link')),
            ('link-info', _('Info link')),
            ('link-light', _('Light link')),
            ('link-dark', _('Dark link')),
            ('nav-link link-primary', _('Primary link, no underline')),
            ('nav-link link-secondary', _('Secondary link, no underline')),
            ('nav-link link-success', _('Success link, no underline')),
            ('nav-link link-danger', _('Danger link, no underline')),
            ('nav-link link-warning', _('Warning link, no underline')),
            ('nav-link link-info', _('Info link, no underline')),
            ('nav-link link-light', _('Light link, no underline')),
            ('nav-link link-dark', _('Dark link, no underline')),
        ],
        default='list-group-item',
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
    badge_location = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Default')),
            ('position-absolute top-0 start-100 translate-middle', _('Top right corner')),
            ('position-absolute top-0 start-0 translate-middle', _('Top left corner')),
            ('position-absolute top-100 start-100 translate-middle', _('Bottom right corner')),
            ('position-absolute top-100 start-0 translate-middle', _('Bottom left corner')),
        ],
        default='',
        label=_('Post number location'),
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
            
        if 'post_list_page' in value and value['post_list_page']:
            category_query = PostCategory.objects.filter(
                id__in=PostPagePostCategory.objects.filter(
                    post_page__in=post_page_model.objects.descendant_of(value['post_list_page']).live()
                ).values('post_category__id').distinct())

            if value['show_badges']:
                category_query = category_query.annotate(num_posts=Count('post_pages'))
        
            if not value['order_by']:
                value['order_by'] = '-created_at'
            category_query = category_query.order_by(value['order_by'])
            
            if value['categories_number'] > 0:
                category_query = category_query[0:value['categories_number']]
                
            
        value['categories'] = category_query
        return super().render(value, context)
        
    class Meta:
        icon = 'list-ul'
        label = _('Categories for posts')
        template = 'waggylabs/blocks/template/post_category_list.html'
        form_template = 'waggylabs/blocks/form_template/post_category_list.html'
        help_text = _('Block to show categories for posts that are childern of the specified post list page. '
                      'If post list page is not specified, the block must be located on a post list page.')