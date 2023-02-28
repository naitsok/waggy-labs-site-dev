from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import ChoiceBlock, TextBlock, StructBlock

from wagtailmarkdown.blocks import render_markdown

# list of pairs for code block; first value must indicate the valid
# codemirror mode file (e.g., stex, clike, etc), https://codemirror.net/5/mode/;
# second value is the display text
CODEBLOCK_LANGS = getattr(
    settings, 
    'WAGGYLABS_CODEBLOCK_LANGS', 
    [
        ('python', _('Python')),
        ('clike', _('C, C++, C#')),
        ('clike', _('Java')),
        ('javascript', _('Javascript')),
        ('xml', _('HTML, XML')),
        ('octave', _('MATLAB')),
        ('mathematica', _('Mathematica')),
        ('r', _('R')),
        ('clike', _('Kotlin')),
        ('swift', _('Swift')),
        ('powershell', _('Powershell')),
        ('sql', _('SQL')),
        ('css', _('CSS')),
    ],
)

class CodeBlock(StructBlock):
    """Code block to enter code with highlighting using CodeMirror editor. According to 
    https://docs.wagtail.org/en/stable/advanced_topics/customisation/streamfield_blocks.html#additional-javascript-on-structblock-forms.
    """
    
    mode = ChoiceBlock(
        choices=(settings.WAGGYLABS_CODEBLOCK_LANGS if
                 hasattr(settings, 'WAGGYLABS_CODEBLOCK_LANGS')
                 else CODEBLOCK_LANGS),
        required=True,
        default='python',
        label=_('Code language'),
        help_text=_('Choose the programming language.'),
    )
    code = TextBlock(
        required=True,
        label=_('Code snippet'),
        help_text=_('Write or paste code.'),
    )
    
    def render_basic(self, value, context=None):
        return render_markdown('```' + value['mode'] +
                               '\n' + value['code'] +
                               '\n```', context)
    
    class Meta:
        icon = 'code'
        label = _('Code')
        label_format = _('Code: {mode}')
    