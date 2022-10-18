from django import forms
from django.conf import settings

from wagtail.core.telepath import register
from wagtail.core.widget_adapters import WidgetAdapter
from wagtail.utils.widgets import WidgetWithScript


DEFAULT_CODEMIRROR_VER = '5.65.9'

class MathJaxMarkdownTextarea(WidgetWithScript, forms.widgets.Textarea):
    """Replaces wagtail-markdown MarkdownTextarea with the one that is able to render MathJax"""
    
    codemirror_ver = settings.WAGGYLABS_CODEMIRROR_VER if hasattr(settings, 'WAGGYLABS_CODEMIRROR_VER') else DEFAULT_CODEMIRROR_VER
    
    """def render_js_init(self, id_, name, value):
        if (
            hasattr(settings, "WAGTAILMARKDOWN")
            and "autodownload_fontawesome" in settings.WAGTAILMARKDOWN
        ):
            autodownload = (
                "true"
                if settings.WAGTAILMARKDOWN["autodownload_fontawesome"]
                else "false"
            )
            return f'easymdeAttach("{id_}", {autodownload});'

        return f'easymdeAttach("{id_}");'"""
    @property
    def media(self):
        """Adds static files nessary for work"""
        
        return forms.Media(
            css={
                "all": (
                    "waggy_labs/css/mathjax_markdown_block/easymde.tweaks.css",
                    "waggy_labs/css/mathjax_markdown_block/easymde.min.css",
                    "waggy_labs/css/mathjax_markdown_block/easymde.hl.css",
                    "https://cdn.jsdelivr.net/highlight.js/latest/styles/github.min.css", # for code highlighting
                )
            },
            js=(
                "waggy_labs/js/mathjax_markdown_block/easymde.min.js",
                "waggy_labs/js/mathjax_markdown_block/easymde.attach.js",
                "https://cdn.jsdelivr.net/highlight.js/latest/highlight.min.js", # for code highlighting
                f"https://cdnjs.cloudflare.com/ajax/libs/codemirror/{self.codemirror_ver}/codemirror.min.js", # For latex highlighting
                f"https://cdnjs.cloudflare.com/ajax/libs/codemirror/{self.codemirror_ver}/mode/stex/stex.min.js", # For latex highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/clike/clike.min.js", # For C++/C/C#/Java/Kotlin highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/css/css.min.js", # For CSS highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/django/django.min.js", # For Django highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/javascript/javascript.min.js", # For Javascript highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/mathematica/mathematica.min.js", # For Mathematica highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/octave/octave.min.js", # For MATLAB/Octave highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/powershell/powershell.min.js", # For Powershell highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/python/python.min.js", # For Python highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/sql/sql.min.js", # For SQL highlighting
                # "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.8/mode/swift/swift.min.js", # For Swift highlighting
                
            ),
        )
        

class MathJaxMarkdownTextareaAdapter(WidgetAdapter):
    """Replaces the markdown-textarea MarkdownTextareaAdapter to have Javascript code from waggy_labs"""
    js_constructor = "waggy_labs.widgets.MarkdownTextarea"

    class Media:
        js = ["waggy_labs/js/mathjax_markdown_block/markdown-textarea-adapter.js"]


register(MathJaxMarkdownTextareaAdapter(), MathJaxMarkdownTextarea)
