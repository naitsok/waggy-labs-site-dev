from django import forms
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import TextBlock

from wagtailmarkdown.blocks import render_markdown

from waggylabs.widgets import MathJaxMarkdownTextarea


class MathJaxMarkdownBlock(TextBlock):
    """Replaces wagtail-markdown MarkdownBlock with this one in order to add LaTeX syntax highlighting
    and MathJax equations rendering during preview."""
    
    def __init__(self,
                 required=True,
                 help_text=_('Use this general text field to write paragraphs using Markdown syntax. '
                             'The links to the pages of this website are added using the specific '
                             'syntax described at https://github.com/torchbox/wagtail-markdown#inline-links. '
                             'Inline and block equation can be added using standard LaTeX syntax, '
                             'references to equation are supproted using \\\u3164ref{...} or '
                             '\\\u3164eqref{...} syntax. Similarly \\\u3164ref{...} and '
                             '\\\u3164cite{...} commands are available to reference figures, '
                             'tables, blockquotes, listings, documents, as well as cite literature. '
                             'Note that final references and citing literature numbers will be '
                             'correctly generated on the published page, which can be previewed '
                             'before publishing Wagtail button at the bottom of the current web page.'),
                 rows=1,
                 max_length=None,
                 min_length=None,
                 validators=(),
                 easymde_min_height='300px', # e.g. 300px, valid CSS string
                 easymde_max_height='500px', # e.g. 500px, valid CSS string
                 easymde_combine='true', # combine or not stex mode with markdown mode
                 # valid string that contains list of valid EasyMDE buttons + math patterns seprated by comma
                 # see the easymde-attach.js for availabe math patterns
                 easymde_toolbar_config=('bold,italic,strikethrough,heading,|,'
                                         'unordered-list,ordered-list,link,|,code,'
                                         'subscript,superscript,equation,matrix,'
                                         'align,|,preview,side-by-side,fullscreen,guide'),
                # status bar: true for default status bar, false for no status bar, 
                # string of comma-separated names for custom status bar
                easymde_status='true',
                 **kwargs):
        self.easymde_min_height = easymde_min_height
        self.easymde_max_height = easymde_max_height
        self.easymde_combine = easymde_combine
        self.easymde_toolbar_config = easymde_toolbar_config
        self.easymde_status = easymde_status
        super().__init__(required, help_text, rows, max_length, min_length, validators, **kwargs)
    
    @cached_property
    def field(self):
        field_kwargs = {
            'widget': MathJaxMarkdownTextarea(attrs={
                'rows': self.rows,
                'easymde-min-height': self.easymde_min_height,
                'easymde-max-height': self.easymde_max_height,
                'easymde-combine': self.easymde_combine,
                'easymde-toolbar': self.easymde_toolbar_config,
                'easymde-status': self.easymde_status,
                })
            }
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)

    def render_basic(self, value, context=None):
        value = value.replace('\r', '')
        return render_markdown(value, context)
    
    class Meta:
        icon = 'doc-full'
