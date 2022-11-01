from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, StructBlock

from .math import MathBlock
from .mathjax_markdown import MathJaxMarkdownBlock


class EquationBlock(StructBlock):
    """A standalone equation block with (skippable) caption. Edit equation via CodeMirror with LaTeX mode. According to 
    https://docs.wagtail.org/en/stable/advanced_topics/customisation/streamfield_blocks.html#additional-javascript-on-structblock-forms.
    """
    equation = MathBlock(
        required=True,
        help_text=_('Write or paste LaTeX style equation (equation, matrix, align, etc. environments are supported).'),
        rows=4
    )
    caption = MathJaxMarkdownBlock(
        required=False,
        help_text=_('Equation caption that will be displayed when the equation is shown in the dialog box.'),
        easymde_min_height='200px',
        easymde_max_height='200px',
        easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,preview,side-by-side,fullscreen,guide',
    )
    anchor = CharBlock(
        max_length=50,
        required=False,
        help_text=_('Anchor link id for referencing in a Markdown block using #anchor. Ignored if \\label{...} is present.')
    )
    
    def render(self, value, context=None):
        equation_string = value['equation'].lower()
        if not equation_string.startswith('\\begin'):
            label = '\n'
            if value['anchor']:
                label = label + '\\label{' + value['anchor'] + '}\n'
            value['equation'] = '\\begin{equation}\n' + value['equation'].trim('$') + label + '\\end{equation}\n'
        else:
            if (not '\\label' in equation_string) and value['anchor']:
                idx = equation_string.find('\\end')
                value['equation'] = value['equation'][:idx] + '\n\\label{' + value['anchor'] + '}\n' + value['equation'][idx:]
        return super().render(value, context)
    
    class Meta:
        icon = 'superscript'
        label = 'Equation'
        template = 'waggy_labs/blocks/equation.html'