from django import forms
from django.conf import settings

from wagtail.telepath import register
from wagtail.widget_adapters import WidgetAdapter
from wagtail.utils.widgets import WidgetWithScript


CODEMIRROR_VERSION = getattr(settings, 'WAGGYLABS_CODEMIRROR_VERSION', '5.65.9')

class MarkdownTextarea(WidgetWithScript, forms.widgets.Textarea):
    """Replaces wagtail-markdown MarkdownTextarea with the one that is able to render MathJax."""
    def __init__(
        self,
        attrs={
            'rows': 1,
            'easymde-min-height': '100px', # e.g. 300px, valid CSS string
            'easymde-max-height': '100px', # e.g. 500px, valid CSS string
            'easymde-combine': 'true', # combine or not stex mode with markdown mode
            # valid string that contains list of valid EasyMDE buttons + math patterns
            # seprated by comma, see the easymde-attach.js for availabe math patterns
            'easymde-toolbar': ('bold,italic,strikethrough,heading,|,'
                                'unordered-list,ordered-list,link,|,code,'
                                'subscript,superscript,equation,matrix,'
                                'align,|,preview,side-by-side,fullscreen,guide'),
            # status bar: true for default status bar, false for no status bar,
            # string of comma-separated names for custom status bar
            'easymde-status': 'true',
        }
    ):
        super().__init__(attrs)

    def render_js_init(self, id_, name, value):
        """Attaches javascript init function to the widget."""
        return f'easymdeAttach("{id_}");'

    @property
    def media(self):
        """Adds static files nessary for work"""
        
        return forms.Media(
            css={
                "all": (
                    "waggylabs/css/widgets/easymde-darkmode.css",
                    "waggylabs/css/widgets/easymde-min.css",
                    "waggylabs/css/widgets/easymde-tweaks.css",
                    "waggylabs/css/widgets/easymde-highlight.css",
                    "https://cdn.jsdelivr.net/highlight.js/latest/styles/github.min.css", # for code highlighting
                )
            },
            js=(
                "https://cdn.jsdelivr.net/highlight.js/latest/highlight.min.js", # for code highlighting
                f"https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/codemirror.min.js", # For latex highlighting
                f"https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/mode/stex/stex.min.js", # For latex highlighting
                "waggylabs/js/widgets/marked-min.js", # for custom markdown to avoid parsing LaTex equations
                "waggylabs/js/widgets/easymde-min.js",
                "waggylabs/js/widgets/easymde-attach.js",
                "waggylabs/js/widgets/markdown.js",
                "waggylabs/js/widgets/markdown-emoji.js",
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
