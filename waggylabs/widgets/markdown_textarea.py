from django import forms
from django.conf import settings

from wagtail.telepath import register
from wagtail.widget_adapters import WidgetAdapter
from wagtail.utils.widgets import WidgetWithScript


CODEMIRROR_VERSION = getattr(settings, 'WAGGYLABS_CODEMIRROR_VERSION', '5.65.9')

class MarkdownTextarea(WidgetWithScript, forms.widgets.Textarea):
    """Replaces wagtail-markdown MarkdownTextarea with the one that is able to render MathJax."""
    
    @property
    def media(self):
        """Adds static files nessary for work"""
        
        return forms.Media(
            css={
                "all": (
                    "waggylabs/css/widgets/easymde-tweaks.css",
                    "waggylabs/css/widgets/easymde-min.css",
                    "waggylabs/css/widgets/easymde-highlight.css",
                    "https://cdn.jsdelivr.net/highlight.js/latest/styles/github.min.css", # for code highlighting
                )
            },
            js=(
                "waggylabs/js/widgets/easymde-min.js",
                "waggylabs/js/widgets/easymde-attach.js",
                "waggylabs/js/widgets/markdown.js",
                "waggylabs/js/widgets/markdown-emoji.js",
                "https://cdn.jsdelivr.net/highlight.js/latest/highlight.min.js", # for code highlighting
                "https://cdn.jsdelivr.net/npm/marked/marked.min.js", # for custom markdown to avoid parsing LaTex equations
                f"https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/codemirror.min.js", # For latex highlighting
                f"https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/mode/stex/stex.min.js", # For latex highlighting
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
    """Replaces the markdown-textarea MarkdownTextareaAdapter to have Javascript code from waggylabs"""
    js_constructor = "waggylabs.widgets.MarkdownTextarea"

    class Media:
        js = ["waggylabs/js/blocks/markdown-adapter.js"]


register(MathJaxMarkdownTextareaAdapter(), MarkdownTextarea)
