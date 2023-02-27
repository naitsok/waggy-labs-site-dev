from django.utils.translation import gettext_lazy as _

from wagtail.blocks import StructBlock, CharBlock, ChoiceBlock

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import LinkStyleChoiceBlock, CardStyleChoiceBlock
from waggylabs.widgets import DisabledOptionSelect


class PostSeriesBlock(StructBlock):
    """Block to display contents for post series. E.g. main post
    and its subposts."""
    style = CardStyleChoiceBlock(
        required=False,
        label=_('Style'),
    )
    header = CharBlock(
        required=False,
        label=_('Header: e.g. "Series"'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('Header icon - start typing'),
    )
    header_icon_location = IconLocationBlock(required=False)
    alignment = ChoiceBlock(
        required=False,
        choices=[
            ('', 'Text alignment'),
            ('text-start', 'Left'),
            ('text-center', 'Center'),
            ('text-end', 'Right'),
        ],
        default='',
        label=_('Text alignment'),
        widget=DisabledOptionSelect,
    )
    post_link_style = LinkStyleChoiceBlock(
        required=False,
        label=_('Post link style'),
    )
    current_post_style = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Current post style')),
            ('fst-normal', 'Default'),
            ('fw-bold', 'Bold'),
            ('fw-bolder', 'Bolder'),
            ('fw-semibold', 'Semibold'),
            ('fw-normal', 'Normal'),
            ('fw-light', 'Light'),
            ('fw-lighter', 'Lighter'),
            ('fst-italic', 'Italic'),
            ('fw-bold fst-italic', 'Bold italic'),
            ('fw-bolder fst-italic', 'Bolder italic'),
            ('fw-semibold fst-italic', 'Semibold italic'),
            ('fw-light fst-italic', 'Light italic'),
            ('fw-lighter fst-italic', 'Lighter italic'),
        ],
        default='',
        label=_('Current post style'),
        widget=DisabledOptionSelect,
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        for block in self.child_blocks.values():
            block.field.widget.attrs.update({
                'placeholder': block.label,
            })

    class Meta:
        icon = 'list-ul'
        label = _('Post series')
        form_template = 'waggylabs/blocks/form_template/post_series.html'
        template = 'waggylabs/blocks/template/post_series.html'
        help_text = _('If the post is included into a series, '
                      'its contents is displayed.')