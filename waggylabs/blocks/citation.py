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
        required=False,
        form_classname='waggylabs-label-cite',
        help_text=_('Cite literature using LaTeX \\cite{...} syntax in text markdown block.')
    )
    
    class Meta:
        icon = 'link'
        label = _('Citation')
        template = 'waggylabs/frontend_blocks/citation.html'
        label_format = _('{citation}')