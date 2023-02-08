
from django.utils.translation import gettext_lazy as _

from wagtail.blocks import (
    StructBlock, BooleanBlock, ChoiceBlock, CharBlock
)

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
            ('', _('Choose time format')),
            ('G:i', _('24-hour format')),
            ('g:i A', _('12-hour format')),
        ],
        label=_('Time format'),
        widget=DisabledOptionSelect,
    )
    header_style = ChoiceBlock(
        required=True,
        choices=[
            ('', 'Choose row header style'),
            ('fst-normal', 'Default'),
            ('fw-bold', 'Bold'),
            ('fw-bolder', 'Bolder'),
            ('fw-semibold', 'Semibold'),
            ('fw-normal', 'Normal'),
            ('fw-light', 'Light'),
            ('fw-lighter', 'Lighter'),
            ('fst-italic', 'Italic'),
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
        label=_('Row header style'),
        widget=DisabledOptionSelect,
    )
    data_style = ChoiceBlock(
        required=True,
        choices=[
            ('', 'Choose row header style'),
            ('fst-normal', 'Default'),
            ('fw-bold', 'Bold'),
            ('fw-bolder', 'Bolder'),
            ('fw-semibold', 'Semibold'),
            ('fw-normal', 'Normal'),
            ('fw-light', 'Light'),
            ('fw-lighter', 'Lighter'),
            ('fst-italic', 'Italic'),
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
            ('link-primary', _('Primary link')),
            ('link-secondary', _('Secondary link')),
            ('link-success', _('Success link')),
            ('link-danger', _('Danger link')),
            ('link-warning', _('Warning link')),
            ('link-info', _('Info link')),
            ('link-light', _('Light link')),
            ('link-dark', _('Dark link')),
        ],
        label=_('Row style'),
        widget=DisabledOptionSelect,
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
    
    