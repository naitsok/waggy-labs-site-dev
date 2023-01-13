
from django import forms

from wagtail.utils.widgets import WidgetWithScript


class ColorInput(WidgetWithScript, forms.widgets.HiddenInput):
    """Widget to select color."""
    template_name = 'waggylabs/widgets/color_input.html'
    
    def __init__(
        self,
        attrs={
            'class': 'waggylabs-color-input',
        }):
        super().__init__(attrs)
    
    @property
    def media(self):
        return forms.Media(
            js=(
                "waggylabs/js/widgets/color-input.js",
            )
        )