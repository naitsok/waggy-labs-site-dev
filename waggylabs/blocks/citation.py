from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, StructBlock
from .label import LabelBlock


class CitationBlock(StructBlock):
    """Block to add one citation with and refence it using LaTeX \cite{...} syntax."""
    citation = CharBlock(
        required=True,
        label=_('Title of the citation.')
    )
    label = LabelBlock(
        max_length=50,
        required=False,
        from_classname='waggylabs-cite',
        help_text=_('Cite literature using LaTeX \\cite{...} syntax in markdown block.')
    )
    
    class Meta:
        icon = 'link'
        label = _('Citation')
        template = 'waggylabs/blocks/citation.html'