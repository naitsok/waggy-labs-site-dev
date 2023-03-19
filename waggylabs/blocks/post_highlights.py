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


class PostHighlightsBlock(StructBlock):
    """Lists the selected numner of posts based on the """
    post_list_page = PageChooserBlock(
        required=False,
        page_type='waggylabs.PostListPage',
        label=_('Root post list page'),
        help_text=_('Shows only posts that are descendant of this page. '
                    'If left empty, posts selected from all the posts are shown.'),
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
    posts_style = ChoiceBlock(
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
        label=_('Post title list style'),
    )
    posts_number = IntegerBlock(
        required=True,
        min_value=0,
        label=_('Number of posts to show'),
        help_text=_('If zero, all post are shown.')
    )
    post_style = ChoiceBlock(
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
        label=_('Post title style'),
    )
    text_wrap = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Text wrap')),
            ('text-nowrap', _('No text wrapping')),
        ],
        default='',
        label=_('Text wrapping'),
    )
    order_by = ChoiceBlock(
        required=False,
        choices=[
            ('created_at', _('Older first')),
            ('-created_at', _('Newer first')),
            ('title', _('By title acsending')),
            ('-title', _('By title descending')),
            ('owner__username', _('By author ascending')),
            ('-owner__username', _('By author descending')),
        ],
        default='-created_at',
        label=_('Posts ordering'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['header'].field.widget.attrs.update({
            'placeholder': self.child_blocks['header'].label,
        })
        
    def render(self, value, context=None):
        post_page_model = apps.get_model('waggylabs', 'PostPage')
        post_query = None
        if 'post_page_list' in value and value['post_page_list']:
            post_query = post_page_model.objects.descendant_of(value['post_list_page']).live()
        else:
            post_query = post_page_model.objects.live()
            
        post_query = post_query.order_by(value['order_by'])
        
        if value['posts_number'] > 0:
            post_query = post_query[0:value['posts_number']]
            
        value['posts'] = post_query
        return super().render(value, context)
    
    class Meta:
        icon = 'list-ol'
        label = _('Post highlights')
        template = 'waggylabs/blocks/template/post_highlights.html'
        form_template = 'waggylabs/blocks/form_template/post_highlights.html'
        help_text = _('Block to show list of post titles sorted according the selected ordering. '
                      'Block can be used, for example to display list of latest blog post '
                      'titles or news.')