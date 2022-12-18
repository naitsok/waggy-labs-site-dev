from django.utils.translation import gettext_lazy as _

from wagtail.blocks import StructBlock

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
        easymde_combine='false',
        easymde_toolbar_config=('subscript,superscript,equation,matrix,'
                                'align,multiline,split,gather,alignat,'
                                'flalign,|,preview,side-by-side,fullscreen'),
        easymde_status='false',
    )
    caption = MathJaxMarkdownBlock(
        required=False,
        label=_('Equation caption'),
        help_text=_('Caption that will be displayed when the equation is shown '
                    'in the dialog box or in the sidebar.'),
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
        form_classname='waggylabs-label-equation',
        help_text=_('Label for the current equation to be used in the markdown block '
                    'for referencing using standard LaTeX \\\u3164ref{...} syntax. '
                    'This label will be added only if no \\\u3164label{...} is found '
                    'within the \\\u3164begin{...}...\\\u3164end{...} statement.'
                    'The final reference processing is happening on the published page, '
                    'which can be checked using "Preview" functionality.'),
    )
    
    def render(self, value, context=None):
        equation_string = value['equation'].lower()
        # First add LaTeX \begin{equation} and \end{equation}
        # if no \begin{...} and \end{...} statements are present
        if not equation_string.startswith('\\begin{'):
            value['equation'] = ('\\begin{equation}\n' + 
                                 value['equation'].trim('$') +
                                 '\\end{equation}\n')
        # then check and add label if no \label{...} is found
        # within begin{...} and \end{...} statements
        equation_string = value['equation'].lower()
        if (not '\\label{' in equation_string) and value['label']:
            idx = equation_string.find('\\end{')
            value['equation'] = (value['equation'][:idx] +
                                    '\n\\label{' + value['label'] +
                                    '}\n' + value['equation'][idx:])
        return super().render(value, context)
    
    class Meta:
        icon = 'superscript'
        label = _('Equation')
        template = 'waggylabs/frontend_blocks/equation.html'
        label_format = _('Equation')