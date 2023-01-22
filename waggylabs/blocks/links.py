from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, CharBlock,
    PageChooserBlock, URLBlock,
    ChoiceBlock, EmailBlock
    )

from waggylabs.blocks.icon import IconBlock
from waggylabs.widgets import DisabledOptionSelect


class StyleChoiceBlock(ChoiceBlock):
    """Block to choose link style (button or link) from 
    Bootstrap styles."""
    def __init__(
        self,
        choices=[
            ('', _('Choose style')),
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


class ExternalLinkBlock(StructBlock):
    """Block to add links to external websites."""
    link = URLBlock(
        required=True,
        label=_('Link to external site'),
    )
    icon = IconBlock(label=_('Icon'))
    style = StyleChoiceBlock()
    text = CharBlock(
        required=False,
        label=_('Text of the link'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['link'].field.widget.attrs.update({
            'placeholder': 'example.com/username',
        })
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Text of the link'),
        })
    
    class Meta:
        icon = 'link-external'
        label = _('External link')
        form_template = 'waggylabs/blocks/external_link.html'
        template = 'waggylabs/frontend_blocks/external_link.html'
        label_format = _('External link')
    
    
class InternalLinkBlock(StructBlock):
    """Block to add links to this website."""
    link = PageChooserBlock(
        label=_('Link to a page of this site')
    )
    icon = IconBlock(label=_('Icon'))
    style = StyleChoiceBlock()
    text = CharBlock(
        required=False,
        label=_('Text instead of page title'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Text instead of page title'),
        })
    
    class Meta:
        icon = 'link'
        label = _('Internal link')
        form_template = 'waggylabs/blocks/internal_link.html'
        template = 'waggylabs/frontend_blocks/internal_link.html'
        label_format = _('Link: {link}')


class IconEmailBlock(StructBlock):
    """Block to add email with a possible icon."""
    email = EmailBlock(
        required=True,
        label=_('Email address'),
    )
    icon = IconBlock(required=False)
    style = StyleChoiceBlock()
    text = CharBlock(
        required=False,
        label=_('Text to be displayed instead of address'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['email'].field.widget.attrs.update({
            'placeholder': 'email@example.com',
        })
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Text to be displayed'),
        })
    
    class Meta:
        icon = 'mail'
        label = _('Email')
        form_template = 'waggylabs/blocks/email.html'
        template = 'waggylabs/frontend_blocks/email.html'
        label_format = _('Email: {email}')
        
        
class InfoTextBlock(StructBlock):
    """Block to add any type of text such as location or phone."""
    text = CharBlock(
        required=True,
        label=_('Phone, address, etc.'),
    )
    icon = IconBlock(required=False)
    style = StyleChoiceBlock()
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['text'].field.widget.attrs.update({
            'placeholder': _('Phone, address, etc.'),
        })
    
    class Meta:
        icon = 'clipboard-list'
        label = _('Phone, address, etc.')
        form_template = 'waggylabs/blocks/info_text.html'
        template = 'waggylabs/frontend_blocks/info_text.html'
        label_format = _('Info: {text}')
        