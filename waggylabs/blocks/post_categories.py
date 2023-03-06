from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    ChoiceBlock, StructBlock, CharBlock, PageChooserBlock
)

from waggylabs.blocks.icon import IconBlock, IconLocationBlock
from waggylabs.blocks.styling import (
    CardStyleChoiceBlock, HeaderStyleChoiceBlock
)
from waggylabs.widgets import DisabledOptionSelect


class PostCategoriesBlock(StructBlock):
    """Block to show post categories."""
    post_list_page = PageChooserBlock(
        required=False,
        page_type='waggylabs.models.post_list_page.PostListPage',
        label=_('Root post list page'),
        help_text=_('Shows post categories for the posts, which are '
                    'children of the selected post list page. '
                    'If left empty, the currently browsed post list page will '
                    'be used, or all categories will be displayed if the '
                    ' currently browsed page is not a post lit page.')
    )
    style = CardStyleChoiceBlock(
        required=False,
        label=_('Style')
    )
    header = CharBlock(
        required=False,
        label=_('Header'),
    )
    header_icon = IconBlock(
        required=False,
        label=_('Header icon - start typing'),
    )
    header_icon_location = IconLocationBlock(
        required=False,
        label=_('Header icon location')
    )
    