
from django.forms import CharField
from django.utils.functional import cached_property

from wagtail.blocks import FieldBlock

from waggylabs.widgets import IconInput


class IconBlock(FieldBlock):
    """Icon block with the IconInput widget."""
    def __init__(
        self,
        required=False,
        help_text=None,
        max_length=None,
        min_length=None,
        validators=(),
        **kwargs,
    ):
        self.field_options = {
            "required": required,
            "help_text": help_text,
            "max_length": max_length,
            "min_length": min_length,
            "validators": validators,
        }
        super().__init__(**kwargs)
    
    @cached_property
    def field(self):
        field_kwargs = { 'widget': IconInput() }
        field_kwargs.update(self.field_options)
        return CharField(**field_kwargs)