
from django.forms import CharField
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import FieldBlock, ChoiceBlock

from waggylabs.widgets import IconInput, DisabledOptionSelect


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
    
    
class IconLocationBlock(ChoiceBlock):
    """Block to choose icon location."""
    def __init__(
        self,
        choices=[
            ('', _('Choose icon location')),
            ('start', _('Before text')),
            ('end', _('After text')),
        ],
        default='',
        label=_('Icon location'),
        required=True,
        help_text=None,
        widget=DisabledOptionSelect,
        validators=(),
        **kwargs):
        super().__init__(
            choices,
            default,
            required,
            help_text,
            widget,
            validators,
            label=label,
            **kwargs)