from django import forms
from django.conf import settings

from wagtail.telepath import register
from wagtail.widget_adapters import WidgetAdapter
from wagtail.utils.widgets import WidgetWithScript


CODEMIRROR_VERSION = getattr(settings, 'WAGGYLABS_CODEMIRROR_VERSION', '5.65.9')

class MathTextarea(WidgetWithScript, forms.widgets.Textarea):
    """Telepath adapter for Textarea to edit LaTeX style equations with CodeMirror."""
    
    @property
    def media(self):
        """Adds static files nessary for work"""
        return forms.Media(
            css={
                "all": (
                    "waggylabs/css/blocks/codemirror-tweaks.css",
                )
            },
            js=(
                f"https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/codemirror.min.js", # For latex highlighting
                f"https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/mode/stex/stex.min.js", # For latex highlighting
            ),
        )
        
class MathTextareaAdapter(WidgetAdapter):
    """Replaces the textarea with MathTextareaAdapter to have Javascript code to use CodeMirror for editing and MathJax for preview."""
    js_constructor = "waggylabs.widgets.MathTextarea"

    class Media:
        js = ["waggylabs/js/blocks/math-adapter.js"]


register(MathTextareaAdapter(), MathTextarea)
