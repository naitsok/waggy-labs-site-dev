
import json
import os
import re

from collections import OrderedDict

from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.telepath import register
from wagtail.widget_adapters import WidgetAdapter
from wagtail.utils.widgets import WidgetWithScript


def collect_icons():
    """Collects icon classes from the CSS file."""
    with open(os.path.join(settings.STATIC_ROOT, 'waggylabs/css/vendor/bootstrap-icons-input.css'), 'r') as f:
        matches = [m.group(0).lstrip('.').rstrip(':')
                for m in re.finditer(r'\.bi-[a-z\-]*\:', f.read())]
    matches.sort()
    d = OrderedDict()
    for m in matches:
        d[m[3:].replace('-', ' ')] = 'bi ' + m
    return d


BOOTSTRAP_ICONS = collect_icons()
class IconInput(WidgetWithScript, forms.widgets.TextInput):
    """Widget to select Font Awesome icon."""
    
    def __init__(
        self,
        icons=BOOTSTRAP_ICONS,
        attrs={
            'placeholder': _('Icon - start typing'),
            'class': 'waggylabs-icon-input',
        }):
        super().__init__(attrs)
        self.attrs['iconsjson'] = json.dumps(icons)
    
    @property
    def media(self):
        return forms.Media(
            css={
                "all": (
                    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css",
                    )
            },
            js=(
                # Wagtail already uses jquery-ui.js so no need to add here
                "waggylabs/js/widgets/icon-input.js",
            )
        )
        
class IconInputAdapter(WidgetAdapter):
    """Replaces the textarea with MathTextareaAdapter to have Javascript code to use CodeMirror for editing and MathJax for preview."""
    js_constructor = "waggylabs.widgets.IconInput"

    class Media:
        js = ["waggylabs/js/blocks/icon-input-adapter.js"]

register(IconInputAdapter(), IconInput)