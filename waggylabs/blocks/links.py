from django.forms import CharField
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (
    StructBlock, CharBlock, ListBlock,
    PageChooserBlock, StreamBlock, URLBlock,
    ChoiceBlock, FieldBlock, EmailBlock
    )

from waggylabs.widgets.editor import (
    DisabledOptionSelect, IconInput
)


class StyleChoiceBlock(ChoiceBlock):
    """Block to choose link style (button or link) from 
    Bootstrap styles."""
    def __init__(
        self,
        choices=[
            ('', _('Choose style')),
            ('btn btn-primary', _('Button')),
            ('card-link', _('Link')),
        ],
        default='',
        label=_('Style of the link'),
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


class ExternalLinkBlock(StructBlock):
    """Block to add links to external websites."""
    link = URLBlock(
        required=True,
        label=_('Link to external site'),
    )
    text = CharBlock(
        required=False,
        label=_('Text of the link'),
    )
    icon = IconBlock(label=_('Icon'))
    style = StyleChoiceBlock()
    
    def render_form_template(self):
        self.child_blocks['link'].field.widget.attrs.update({
            'placeholder': 'twitter.com/username',
        })
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Text of the link'),
        })
        return super().render_form_template()
    
    class Meta:
        icon = 'link-external'
        label = _('External link')
        form_template = 'waggylabs/blocks/external_link.html'
        template = 'waggylabs/frontend_blocks/external_link.html'
    
    
class InternalLinkBlock(StructBlock):
    """Block to add links to this website."""
    link = PageChooserBlock(
        label=_('Link to a page of this site')
    )
    text = CharBlock(
        required=False,
        label=_('Text instead of page title'),
    )
    icon = IconBlock(label=_('Icon'))
    style = StyleChoiceBlock()
    
    def render_form_template(self):
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Text instead of page title'),
        })
        return super().render_form_template()
    
    class Meta:
        icon = 'link'
        label = _('Internal link')
        form_template = 'waggylabs/blocks/internal_link.html'
        template = 'waggylabs/frontend_blocks/internal_link.html'


class IconEmailBlock(StructBlock):
    """Block to add email with a possible icon."""
    email = EmailBlock(
        required=True,
        label=_('Email address'),
    )
    text = CharBlock(
        required=False,
        label=_('Text to be displayed instead of address'),
    )
    icon = IconBlock(required=False)
    style = StyleChoiceBlock()
    
    def render_form_template(self):
        self.child_blocks['email'].field.widget.attrs.update({
            'placeholder': 'email@example.com',
        })
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Text to be displayed'),
        })
        return super().render_form_template()
    
    class Meta:
        icon = 'mail'
        label = _('Email')
        form_template = 'waggylabs/blocks/email.html'
        template = 'waggylabs/frontend_blocks/email.html'
        
        
class InfoTextBlock(StructBlock):
    """Block to add any type of text such as location or phone."""
    text = CharBlock(
        required=True,
        label=_('Phone, address, etc.'),
    )
    icon = IconBlock(required=False)
    style = StyleChoiceBlock()
    
    def render_form_template(self):
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Phone, address, etc.'),
        })
        return super().render_form_template()
    
    class Meta:
        icon = 'clipboard-list'
        label = _('Phone, address, etc.')
        form_template = 'waggylabs/blocks/info_text.html'
        template = 'waggylabs/frontend_blocks/info_text.html'
        