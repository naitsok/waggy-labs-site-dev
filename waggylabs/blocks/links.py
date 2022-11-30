from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import (
    StructBlock, CharBlock, ListBlock,
    PageChooserBlock, StreamBlock, URLBlock,
    ChoiceBlock
    )


class StyleChoiceBlock(ChoiceBlock):
    """Block to choose link style (button or link) from 
    Bootstrap styles."""
    def __init__(
        self,
        choices=[
            ('btn btn-primary', _('Button')),
            ('card-link', _('Link')),
        ],
        default='card-link',
        label=_('Style of link'),
        required=True,
        help_text=None,
        widget=None,
        validators=...,
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
    text = CharBlock(
        required=True,
        label=_('Text of the link'),
    )
    style = StyleChoiceBlock()
    
    class Meta:
        icon = 'link'
        label = _('External link')
        form_template = 'waggylabs/blocks/form_external_link.html'
    
    
class InternalLinkBlock(StructBlock):
    """Block to add links to this website."""
    link = PageChooserBlock(
        label=_('Link to this site page')
    )
    text = CharBlock(
        required=True,
        label=_('Text of the link'),
    )
    style = StyleChoiceBlock()
    
    class Meta:
        icon = 'link'
        label = _('Internal link')
        form_template = 'waggylabs/blocks/form_internal_link.html'
    
    
class SocialLinkBlock(StructBlock):
    """Block to add links to social websites."""
    title = CharBlock(
        max_length=255,
        required=True,
        help_text=_('Title of the social website. For example, Instagram.'),
        label=_('Title of the social website.')
    )
    username = CharBlock(
        max_length=255,
        required=True,
        help_text=_('Username for the social website.'),
        label=_('Username for the social website')
    )
    username_prefix = CharBlock(
        max_length=10,
        required=False,
        help_text=_('Additional prefix before the username if display username is selects. For example "@" for Twitter.'),
        label=_('Prefix for the username')
    )
    icon = CharBlock(
        max_length=255,
        required=False,
        help_text=_('Icon name from Font Awesome website. If left blank, title will used.'),
        label=_('Icon name from Font Awesome website')
    )
    domain = CharBlock(
        max_length=10,
        required=False,
        help_text=_('Domain name for the social website. If left blank, "com" will be used.'),
        label=_('Domain name for the social website')
    )
    view_style = ChoiceBlock(
        choices=[
            ('icon', _('Only social netwok icon')),
            ('title', _('Title of the social website')),
            ('username', _('Username in the social website')),
        ],
        default='username',
        label=_('Text of the link')
    )
    style = StyleChoiceBlock()
    
    class Meta:
        icon = 'link'
        label = _('Social link')
        form_template = 'waggylabs/blocks/form_social_link.html'