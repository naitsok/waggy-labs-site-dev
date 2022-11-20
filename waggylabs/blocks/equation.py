from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock, StructBlock

from .mathjax_markdown import MathJaxMarkdownBlock
from .label import LabelBlock


class EquationBlock(StructBlock):
    """A standalone equation block with (skippable) caption. Edit equation via CodeMirror with LaTeX mode. According to 
    https://docs.wagtail.org/en/stable/advanced_topics/customisation/streamfield_blocks.html#additional-javascript-on-structblock-forms.
    """
    equation = MathJaxMarkdownBlock(
        required=True,
        help_text=_('Write or paste LaTeX style equation (equation, '
                    'matrix, align, etc. environments are supported).'),
        easymde_min_height='150px',
        easymde_max_height='150px',
        easymde_combine='true',
        easymde_toolbar_config=('subscript,superscript,equation,matrix,'
                                'align,multiline,split,gather,alignat,'
                                'flalign,|,preview,side-by-side,fullscreen'),
        easymde_status='false',
    )
    caption = MathJaxMarkdownBlock(
        required=False,
        label=_('Equation caption'),
        # help_text=_('Equation caption that will be displayed when the equation is shown in the dialog box.'),
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
    )
    
    def render(self, value, context=None):
        equation_string = value['equation'].lower()
        if not equation_string.startswith('\\begin'):
            label = '\n'
            if value['anchor']:
                label = label + '\\label{' + value['anchor'] + '}\n'
            value['equation'] = ('\\begin{equation}\n' + 
                                 value['equation'].trim('$') + 
                                 label + '\\end{equation}\n')
        else:
            if (not '\\label' in equation_string) and value['anchor']:
                idx = equation_string.find('\\end')
                value['equation'] = (value['equation'][:idx] + 
                                     '\n\\label{' + value['anchor'] + 
                                     '}\n' + value['equation'][idx:])
        return super().render(value, context)
    
    class Meta:
        icon = 'superscript'
        label = 'Equation'
        template = 'waggylabs/blocks/equation.html'