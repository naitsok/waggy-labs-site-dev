from django import forms
from django.utils.functional import cached_property

from wagtail.core.blocks import TextBlock

from wagtailmarkdown.blocks import render_markdown

from waggy_labs.widgets import MathJaxMarkdownTextarea


class MathJaxMarkdownBlock(TextBlock):
    """Replaces wagtail-markdown MarkdownBlock with this one in order to add LaTeX syntax highlighting
    and MathJax equations rendering during preview."""
    
    def __init__(self,
                 required=True,
                 help_text=None,
                 rows=1,
                 max_length=None,
                 min_length=None,
                 validators=(),
                 easymde_min_height="", # e.g. 300px, valid CSS string
                 easymde_max_height="", # e.g. 500px, valid CSS string
                 easymde_toolbar_config="", # valid string that contains list of valid EasyMDE icons seprated by comma
                 **kwargs):
        self.easymde_min_height = easymde_min_height
        self.easymde_max_height = easymde_max_height
        self.easymde_toolbar_config = easymde_toolbar_config
        super().__init__(required, help_text, rows, max_length, min_length, validators, **kwargs)
    
    @cached_property
    def field(self):
        field_kwargs = {
            "widget": MathJaxMarkdownTextarea(attrs={
                "rows": self.rows,
                "easymde-min-height": self.easymde_min_height,
                "easymde-max-height": self.easymde_max_height,
                "easymde-toolbar": self.easymde_toolbar_config,
                })
            }
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)

    def render_basic(self, value, context=None):
        # making LateX backslashes compatible with markdown escaping
        # value = value.replace('\\\\', '\\\\\\\\') # .replace('\\[', '\\\\[').replace('\\]', '\\\\]').replace('\\)', '\\\\)').replace('\\(', '\\\\(')
        value = value.replace('\r', '')
        return render_markdown(value, context)
    
    class Meta:
        icon = 'doc-full'
