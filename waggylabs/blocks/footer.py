from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, ChoiceBlock
)

from waggylabs.blocks.post_highlights import PostHighlightsBlock


class FooterWidthBlock(StructBlock):
    """Block for footer offset and width. Common for all
    footer blocks."""
    col_offset = ChoiceBlock(
        required=False,
        choices=[
            ('', _('No offset')),
            ('offset-lg-1', _('Narrow')),
            ('offset-lg-2', _('Medium')),
            ('offset-lg-3', _('Wide')),
        ],
        default='',
        label=_('Offset'),
    )
    col_width = ChoiceBlock(
        required=True,
        choices=[
            ('col-lg-2', _('Narrow')),
            ('col-lg-3', _('Medium')),
            ('col-lg-4', _('Wide')),
        ],
        default='col-lg-2',
        label=_('Width'),
    )
    


class FooterPostHighlightsBlock(StructBlock):
    """Footer block to show post highlights."""
    settings = FooterWidthBlock(
        label=_('Footer block settings'),
    )
    post_highlights = PostHighlightsBlock(
        label=_('Post highlights settings'),
        help_text=_('Some of the post highlights settings will be ignored to '
                    'keep styling of footer consistent.'),
    )
    
    class Meta:
        icon = 'list-ol'
        label = _('Post highlights')
        template = 'waggylabs/blocks/template/footer_post_highlights.html'
        # form_template = 'waggylabs/blocks/form_template/footer_post_highlights.html'
        help_text = _('Block to show list of post titles sorted according the selected ordering. '
                      'Block can be used, for example to display list of latest blog post '
                      'titles or news.')