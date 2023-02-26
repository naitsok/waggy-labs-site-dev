
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, BooleanBlock, ChoiceBlock, CharBlock
)

from waggylabs.blocks.styling import TextStyleChoiceBlock
from waggylabs.widgets import DisabledOptionSelect


class PageInfoBlock(StructBlock):
    """A block to show page details such as author, creation
    date, etc. Rendered as a description list. Can be used in
    Sidebar."""
    show_user = BooleanBlock(
        required=False,
        label=_('Show the name of page creator'),
    )
    user_header = CharBlock(
        required=False,
        label=_('Header of the page creator row'),
        help_text=_('Displays the header of the row '
                    'in which the page creator name is '
                    'displayed.'),
    )
    show_email = BooleanBlock(
        required=False,
        label=_('Show the email of page creator'),
    )
    email_header = CharBlock(
        required=False,
        label=_('Header of the page creator email row'),
        help_text=_('Displays the header of the row '
                    'in which the page creator email is '
                    'displayed.'),
    )
    show_first_published_at = BooleanBlock(
        required=False,
        label=_('Date of page creation'),
    )
    first_published_at_header = CharBlock(
        required=False,
        label=_('Header of the page creation date'),
        help_text=_('Displays the header of the row '
                    'in which the page creator date is '
                    'displayed.'),
    )
    show_last_published_at = BooleanBlock(
        required=False,
        label=_('Date of last page update'),
    )
    last_published_at_header = CharBlock(
        required=False,
        label=_('Header of last page update'),
        help_text=_('Displays the header of the row '
                    'in which the last page update is '
                    'displayed.'),
    )
    show_time = BooleanBlock(
        required=False,
        label=_('Show time in the date fields'),
    )
    time_format = ChoiceBlock(
        required=False,
        choices=[
            ('', _('Time format')),
            ('G:i', _('24-hour format')),
            ('g:i A', _('12-hour format')),
        ],
        label=_('Time format'),
        widget=DisabledOptionSelect,
    )
    header_style = TextStyleChoiceBlock(
        required=True,
        label=_('Header style'),
    )
    data_style = TextStyleChoiceBlock(
        required=True,
        label=_('Row style'),
    )
    
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        self.child_blocks['user_header'].field.widget.attrs.update({
            'placeholder': self.child_blocks['user_header'].label,
        })
        self.child_blocks['email_header'].field.widget.attrs.update({
            'placeholder': self.child_blocks['email_header'].label,
        })
        self.child_blocks['first_published_at_header'].field.widget.attrs.update({
            'placeholder': self.child_blocks['first_published_at_header'].label,
        })
        self.child_blocks['last_published_at_header'].field.widget.attrs.update({
            'placeholder': self.child_blocks['last_published_at_header'].label,
        })
        
    def render(self, value, context):
        owner = context['page'].owner
        value['show_header'] = value['user_header'] or value['email_header'] or \
            value['first_published_at_header'] or value['last_published_at_header']
        value['dd_width'] = 'col-sm-8' if value['show_header'] else 'col-sm-12'
        value['username'] = owner.get_username()
        value['full_name'] = owner.get_full_name()
        value['email'] = owner.email
        value['first_published_at'] = context['page'].first_published_at
        value['last_published_at'] = context['page'].last_published_at
        return super().render(value, context)
    
    class Meta:
        icon = 'form'
        label = _('Page info')
        template = 'waggylabs/blocks/template/page_info.html'
        form_template = 'waggylabs/blocks/form_template/page_info.html'
        help_text = _('Page info block displays the information about '
                      'page creator, created date, and last updated date.')
    
    