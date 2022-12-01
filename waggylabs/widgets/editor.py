from django.forms.widgets import Select


class DisabledOptionSelect(Select):
    """Select with disabled option, which value equals to
    empty string."""
    option_template_name = 'waggylabs/widgets/select_option.html'