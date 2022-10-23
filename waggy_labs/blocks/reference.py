from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, StructBlock


class ReferenceBlock(StructBlock):
    """Block to add one reference with a reference link specified by #anchor"""
    reference = CharBlock(
        required=True,
        help_text=_('Reference text.')
    )
    anchor = CharBlock(
        max_length=50,
        required=False,
        help_text=_('Anchor link id for referencing in a Markdown block using #anchor.')
    )
    
    class Meta:
        icon = 'link'
        label = 'Reference'
        template = 'waggy_labs/blocks/reference.html'