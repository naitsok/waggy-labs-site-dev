
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StreamBlock, StructBlock, BooleanBlock, ChoiceBlock, CharBlock
)

from waggylabs.blocks.mathjax_markdown import MathJaxMarkdownBlock
from waggylabs.blocks.sidebar_tabs import SidebarTabsBlock


class SidebarPageDetails(StructBlock):
    """A sidebar block to show page details such as author, creation
    date, etc."""
    pass