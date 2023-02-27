from django.utils.translation import gettext_lazy as _

from wagtail.blocks import ChoiceBlock

from waggylabs.widgets import DisabledOptionSelect


class LinkStyleChoiceBlock(ChoiceBlock):
    """Block to choose link style (button or link) from 
    Bootstrap styles."""
    def __init__(
        self,
        choices=[
            ('', _('Link style')),
            ('btn btn-primary', _('Button primary')),
            ('btn btn-secondary', _('Button secondary')),
            ('btn btn-success', _('Button success')),
            ('btn btn-danger', _('Button danger')),
            ('btn btn-warning', _('Button warning')),
            ('btn btn-info', _('Button info')),
            ('btn btn-outline-primary', _('Button outline primary')),
            ('btn btn-outline-secondary', _('Button outline secondary')),
            ('btn btn-outline-success', _('Button outline success')),
            ('btn btn-outline-danger', _('Button outline danger')),
            ('btn btn-outline-warning', _('Button outline warning')),
            ('btn btn-outline-info', _('Button outline info')),
            ('card-link', _('Card link')),
            ('nav-link', _('Navigation bar link')),
            ('nav-link active', _('Navigation bar active link')),
            ('link-primary', _('Primary link')),
            ('link-secondary', _('Secondary link')),
            ('link-success', _('Success link')),
            ('link-danger', _('Danger link')),
            ('link-warning', _('Warning link')),
            ('link-info', _('Info link')),
            ('link-light', _('Light link')),
            ('link-dark', _('Dark link')),
        ],
        default='',
        label=_('Link style'),
        required=True,
        help_text=None,
        widget=DisabledOptionSelect,
        validators=(),
        **kwargs):
        choices[0] = ('', label)
        super().__init__(
            choices,
            default,
            required,
            help_text,
            widget,
            validators,
            label=label,
            **kwargs)
        
        
class TextStyleChoiceBlock(ChoiceBlock):
    """Block to choose style for text for different blocks."""
    def __init__(
        self,
        choices=[
            ('', 'Text style'),
            ('fst-normal', 'Default'),
            ('fw-bold', 'Bold'),
            ('fw-bolder', 'Bolder'),
            ('fw-semibold', 'Semibold'),
            ('fw-normal', 'Normal'),
            ('fw-light', 'Light'),
            ('fw-lighter', 'Lighter'),
            ('fst-italic', 'Italic'),
            ('fw-bold fst-italic', 'Bold italic'),
            ('fw-bolder fst-italic', 'Bolder italic'),
            ('fw-semibold fst-italic', 'Semibold italic'),
            ('fw-light fst-italic', 'Light italic'),
            ('fw-lighter fst-italic', 'Lighter italic'),
            ('btn btn-primary', _('Button primary')),
            ('btn btn-secondary', _('Button secondary')),
            ('btn btn-success', _('Button success')),
            ('btn btn-danger', _('Button danger')),
            ('btn btn-warning', _('Button warning')),
            ('btn btn-info', _('Button info')),
            ('btn btn-outline-primary', _('Button outline primary')),
            ('btn btn-outline-secondary', _('Button outline secondary')),
            ('btn btn-outline-success', _('Button outline success')),
            ('btn btn-outline-danger', _('Button outline danger')),
            ('btn btn-outline-warning', _('Button outline warning')),
            ('btn btn-outline-info', _('Button outline info')),
        ],
        default='',
        label=_('Text style'),
        required=True,
        help_text=None,
        widget=DisabledOptionSelect,
        validators=(),
        **kwargs):
        choices[0] = ('', label)
        super().__init__(
            choices,
            default,
            required,
            help_text,
            widget,
            validators,
            label=label,
            **kwargs)
        
        
class CardStyleChoiceBlock(ChoiceBlock):
    """Block to choose style of Bootstrap card."""
    def __init__(
        self,
        choices=[
            ('', _('Card style')),
            ('text-bg-primary', _('Primary')),
            ('text-bg-secondary', _('Secondary')),
            ('text-bg-success', _('Success')),
            ('text-bg-danger', _('Danger')),
            ('text-bg-warning', _('Warning')),
            ('text-bg-info', _('Info')),
            ('text-bg-light', _('Light')),
            ('text-bg-dark', _('Dark')),
            ('border-primary', _('Border primary')),
            ('border-secondary', _('Border secondary')),
            ('border-success', _('Border success')),
            ('border-danger', _('Border danger')),
            ('border-warning', _('Border warning')),
            ('border-info', _('Border info')),
            ('border-light', _('Border light')),
            ('border-dark', _('Border dark')),
        ],
        default='',
        label=_('Card style'),
        required=True,
        help_text=None,
        widget=DisabledOptionSelect,
        validators=(),
        **kwargs):
        choices[0] = ('', label)
        super().__init__(
            choices,
            default,
            required,
            help_text,
            widget,
            validators,
            label=label,
            **kwargs)