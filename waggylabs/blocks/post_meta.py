from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, BooleanBlock, ChoiceBlock, CharBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import LinkStyleChoiceBlock, TextStyleChoiceBlock
from waggylabs.widgets import DisabledOptionSelect

class SiblingPostBlock(StructBlock):
    """Defines the appearance of previous and next posts in
    the post footer block."""
    header = CharBlock(
        required=False,
        label=_('Header: e.g. "sibling post"'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('sibling post icon - start typing'),
    )
    header_icon_location = IconLocationBlock(required=False)
    style = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Choose style')),
            ('text-bg-primary', _('Primary')),
            ('text-bg-secondary', _('Secondary')),
            ('text-bg-success', _('Success')),
            ('text-bg-danger', _('Danger')),
            ('text-bg-warning', _('Warning')),
            ('text-bg-info', _('Info')),
            ('text-bg-light', _('Light')),
            ('text-bg-dark', _('Dark')),
            ('border-primary', _('Border primary')),
            ('border-secondary', _('Border secondary')),
            ('border-success', _('Border success')),
            ('border-danger', _('Border danger')),
            ('border-warning', _('Border warning')),
            ('border-info', _('Border info')),
            ('border-light', _('Border light')),
            ('border-dark', _('Border dark')),
        ],
        default='',
        label=_('sibling post style'),
        widget=DisabledOptionSelect,
    )
    alignment = ChoiceBlock(
        required=False,
        choices=[
            ('', 'Choose text alignment'),
            ('text-start', 'Left'),
            ('text-center', 'Center'),
            ('text-end', 'Right'),
        ],
        default='',
        label=_('sibling post text alignment'),
        widget=DisabledOptionSelect,
    )
    
    def __init__(self, post_label, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
            block.label = block.label.replace('sibling', post_label)
            block.field.widget.attrs.update({
                'placeholder': block.label,
            })
            
    class Meta:
        icon = 'list-ul'
        form_template = 'waggylabs/blocks/form_template/sibling_post.html'

class PostMetaBlock(StructBlock):
    """Post meta block describes post metadata, e.g. post author,
    post siblings, tags, categories. If it is las block in BodyBlock,
    then it is displayed after references."""
    show_categories = BooleanBlock(
        required=False,
        default=True,
        label=_('Show post categories'),
    )
    categories_header = CharBlock(
        required=False,
        label=_('Categories header'),
        help_text=_('Text to display before categories list.')
    )
    categories_header_style = TextStyleChoiceBlock(
        required=False,
        label=_('Categories header style'),
    )
    categories_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Categories link style')
    )
    show_tags = BooleanBlock(
        required=False,
        default=True,
        label=_('Show post tags'),
    )
    tags_header = CharBlock(
        required=False,
        label=_('Tags header'),
        help_text=_('Text to display before tag list.')
    )
    tags_header_style = TextStyleChoiceBlock(
        required=False,
        label=_('Tags header style'),
    )
    tags_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Tags link style')
    )
    show_sibling_posts = BooleanBlock(
        required=False,
        default=True,
        label=_('Show previous and next posts'),
        help_text=_(
            'Shows previous and next posts for the current post. '
            'Previous means either previously (chronologically) published or '
            'previous post from the series. Next means either (chronologically) '
            'published next or next post from the series.'
        ),
    )
    previous_post = SiblingPostBlock('Previous')
    next_post = SiblingPostBlock('Next')
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
    
    def render(self, value, context):
        value['show_header'] = value['categories_header'] or value['tags_header']
        value['dd_width'] = 'col-sm-8' if value['show_header'] else 'col-sm-12'
        value['show_sibling_posts'] = value['show_sibling_posts'] and \
            (context['previous_post'] or context['next_post'])
        value['next_post_style'] = value['next_post']['style']
        
        return super().render(value, context)
    
    class Meta:
        label = _('Post metadata')
        icon = 'doc-full-inverse'
        template = 'waggylabs/blocks/template/post_meta.html'
        help_text = _('Post metadata block displays information '
                      'about the post, such as tags, categories, '
                      'links to previous and next posts. If this block '
                      'is at the end, it will be rendered after (possible) '
                      'references.')