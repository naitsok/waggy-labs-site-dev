
from django.utils.translation import gettext_lazy as _

from wagtail.documents.blocks import DocumentChooserBlock

from .label import LabelBlock

class DocumentBlock():
    """Block to add documents and cite them using \cite{...} syntax."""
    document = DocumentChooserBlock()
    label = LabelBlock(
        required=False,
        form_classname='waggylabs-label-cite',
        help_text=_('Cite documents using LaTeX \\cite{...} syntax in text markdown block.')
    )
    
    class Meta:
        icon = 'document'
        label = _('Document')
        template = 'waggylabs/frontend_blocks/document.html'