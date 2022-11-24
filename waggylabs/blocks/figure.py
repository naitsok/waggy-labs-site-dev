from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock

from .mathjax_markdown import MathJaxMarkdownBlock
from .label import LabelBlock


class FigureBlock(StructBlock):
    """Image with caption for StreamField."""
    image = ImageChooserBlock(
        required=True,
        label=_('Graphic'),
        )
    caption = MathJaxMarkdownBlock(
        required=False,
        label=_('Figure caption'),
        help_text='',
        easymde_min_height='100px',
        easymde_max_height='100px',
        easymde_combine='true',
        easymde_toolbar_config=('bold,italic,strikethrough,|,unordered-list,'
                                'ordered-list,link,|,code,subscript,superscript,|,'
                                'preview,side-by-side,fullscreen,guide'),
        easymde_status='false',
    )
    label = LabelBlock(
        max_length=50,
        required=False,
        form_classname='waggylabs-label-figure', # needed to render figure numbers
    )
    
    class Meta:
        template = 'waggylabs/blocks/figure.html'
        icon = 'image'
        label = 'Figure'