from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, BooleanBlock, CharBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import (
    LinkStyleChoiceBlock, TextStyleChoiceBlock, CardStyleChoiceBlock, 
    TextAlignmentChoiceBlock
)

class SiblingPostBlock(StructBlock):
    """Defines the appearance of previous and next posts in
    the post footer block."""
    style = CardStyleChoiceBlock(required=False)
    header = CharBlock(
        required=False,
        label=_('Header: e.g. "Next post"'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('Header icon - start typing'),
    )
    header_icon_location = IconLocationBlock(required=False)
    alignment = TextAlignmentChoiceBlock(required=False)
    post_link_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Post link style'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
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
    style = CardStyleChoiceBlock(required=False)
    header = CharBlock(
        required=False,
        label=_('Header'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('Header icon - start typing'),
    )
    header_icon_location = IconLocationBlock(required=False)
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
    previous_post = SiblingPostBlock()
    next_post = SiblingPostBlock()
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
            if block.name != 'previous_post' and block.name != 'next_post':
                block.field.widget.attrs.update({
                    'placeholder': block.label,
                })
    
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
        form_template = 'waggylabs/blocks/form_template/post_meta.html'
        help_text = _('Post metadata block displays information '
                      'about the post, such as tags, categories, '
                      'links to previous and next posts. If this block '
                      'is at the end, it will be rendered after (possible) '
                      'references.')