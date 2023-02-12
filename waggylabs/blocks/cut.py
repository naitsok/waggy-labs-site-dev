
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, CharBlock, ChoiceBlock
)

from waggylabs.widgets import DisabledOptionSelect
from .icon import IconBlock, IconLocationBlock
from .link_style import LinkStyleChoiceBlock

class CutBlock(StructBlock):
    """Block to cut the page content after it. For example,
    when page shows up in a list such as pagination or search.
    The cut button redirects to the full page."""
    text = CharBlock(
        required=False,
        label=_('Text on the cut button'),
    )
    style = LinkStyleChoiceBlock()
    icon = IconBlock(required=False)
    icon_location = IconLocationBlock(required=False)
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': self.child_blocks['text'].label,
        })
    
    class Meta:
        icon = 'arrow-right'
        label = _('Cut')
        label_format = _('Cut: {text}')
        template = 'waggylabs/blocks/template/cut.html'
        form_template = 'waggylabs/blocks/form_template/cut.html'
        help_text = _('Block to cut the page content after it. For example, '
                      'when page shows up in a list such as pagination or search. '
                      'The cut button redirects to the full page.')