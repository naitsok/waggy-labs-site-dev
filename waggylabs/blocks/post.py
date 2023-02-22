from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, BooleanBlock, ChoiceBlock, CharBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.widgets import DisabledOptionSelect


class PostFooterBlock(StructBlock):
    """Post footer block defines how post siblings, tags and
    categories are displayed on the PostPage."""
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
    previous_post_title = CharBlock(
        required=False,
        label=_('Title for "previous post" text'),
        help_text=_('Title for the previous post, e.g. "Previous post".')
    )
    previous_post_icon = IconBlock(
        required=False,
        label=_('Previous post icon')
    )
    previous_post_icon_location = IconLocationBlock(required=False)
    previous_post_style = ChoiceBlock(
        required=True,
        choices=[
            ('', _('Choose previous post style')),
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
        label=_('Previous post style'),
        widget=DisabledOptionSelect,
    )
    previous_post_alignment = ChoiceBlock(
        required=True,
        choices=[
            ('', 'Choose text alignment for previous post'),
            ('text-start', 'Left'),
            ('text-center', 'Center'),
            ('text-end', 'Right'),
        ],
        default='',
        label=_('Previous post text alignment'),
        widget=DisabledOptionSelect,
    )
    next_post_title = CharBlock(
        required=False,
        label=_('Title for "next post" text'),
        help_text=_('Title for the next post, e.g. "Next post".')
    )
    next_post_icon = IconBlock(
        required=False,
        label=_('Previous post icon')
    )
    next_post_icon_location = IconLocationBlock(required=False)
    next_post_alignment = ChoiceBlock(
        required=True,
        choices=[
            ('', 'Choose text alignment for next post'),
            ('text-start', 'Left'),
            ('text-center', 'Center'),
            ('text-end', 'Right'),
        ],
        default='',
        label=_('Next post text alignment'),
        widget=DisabledOptionSelect,
    )