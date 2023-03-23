from django.utils.translation import gettext_lazy as _

from wagtail.blocks import StructBlock, CharBlock, ChoiceBlock

from waggylabs.blocks.card_header import CardHeaderBlock
from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import (
    LinkStyleChoiceBlock, CardStyleChoiceBlock, TextAlignmentChoiceBlock,
    TextStyleChoiceBlock
)
from waggylabs.blocks.wrapper import WrapperBlock


class PostSeriesItemBlock(StructBlock):
    """Item block to display contents for post series. E.g. main post
    and its subposts."""
    post_link_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Post link style'),
    )
    current_post_style = TextStyleChoiceBlock(
        label=_('Current post style'),
    )

    class Meta:
        icon = 'list-ul'
        label = _('Post series')
        form_template = 'waggylabs/blocks/form_template/post_series.html'
        template = 'waggylabs/blocks/template/post_series.html'


class PostSeriesBlock(WrapperBlock):
    """Block to display contents for post series. E.g. main post
    and its subposts."""
    item = PostSeriesItemBlock()
    
    class Meta:
        icon = 'list-ul'
        label = _('Post series')
        help_text = _('If the post is included into a series, '
                      'its title appears in this block. The currenlty '
                      'shown post is highlihted according to the selected style.')