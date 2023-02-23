from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, BooleanBlock, ChoiceBlock, CharBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.page_info import PageInfoBlock
from waggylabs.blocks.styling import LinkStyleChoiceBlock, TextStyleChoiceBlock
from waggylabs.widgets import DisabledOptionSelect

class SiblingPostBlock(StructBlock):
    """Defines the appearance of previous and next posts in
    the post footer block."""
    sibling_post_title = CharBlock(
        required=False,
        label=_('Title for "sibling post" text'),
        help_text=_('Title for the sibling post, e.g. "sibling post".')
    )
    sibling_post_icon = IconBlock(
        required=False,
        label=_('sibling post icon')
    )
    sibling_post_icon_location = IconLocationBlock(required=False)
    sibling_post_style = ChoiceBlock(
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
    sibling_post_alignment = ChoiceBlock(
        required=False,
        choices=[
            ('', 'Choose text alignment'),
            ('text-start', 'Left'),
            ('text-center', 'Center'),
            ('text-end', 'Right'),
        ],
        default='',
        label=_('Sibling post text alignment'),
        widget=DisabledOptionSelect,
    )
    def __init__(self, post_label, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
            block.label = block.label.replace('sibling', post_label)

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
    
    def render(self, value, context=None):
        value['show_header'] = value['categories_header'] or value['tags_header']
        value['dd_width'] = 'col-sm-8' if value['show_header'] else 'col-sm-12'
        
        return super().render(value, context)
    
    class Meta:
        label = _('Post metadata')
        icon = 'form'
        template = 'waggylabs/blocks/template/page_meta.html'
        help_text = _('Post metadata block displays information '
                      'about the post, such as tags, categories, '
                      'links to previous and next posts.')