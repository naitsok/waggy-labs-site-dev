from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, StructBlock
from .label import LabelBlock


class CitationBlock(StructBlock):
    """Block to add one citation with and refence it using LaTeX \cite{...} syntax."""
    citation = CharBlock(
        required=True,
        label=_('Title of the citation.'),
    )
    label = LabelBlock(
        required=False,
        form_classname='waggylabs-label-cite',
        help_text=_('Cite literature using LaTeX \\cite{...} syntax in text markdown block.'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['citation'].field.widget.attrs.update({
            'placeholder': 'e.g. Author A, Author B, Title, Year, Journal.',
        })
    
    class Meta:
        icon = 'link'
        label = _('Citation')
        template = 'waggylabs/frontend_blocks/citation.html'
        form_template = 'waggylabs/blocks/citation.html'
        label_format = _('Cite: {citation}')