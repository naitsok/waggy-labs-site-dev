from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import CharBlock


class LabelBlock(CharBlock):
    """LabelBlock to add labels to figures, tables, references, etc,
    for referencing them in e.g. Markdown text using standard LaTex
    \ref{...} syntax. LabelBlock adds the specific CSS class to the
    standard Wagtail CharBlock. The CSS class will be used to select
    all the LabelBlocks by javascript selector for reference processing
    for the final view of the page."""
    def __init__(self,
                 required=False,
                 help_text=_('Label for the current entity (figure, table, equation) '
                             'to be used in the markdown block for referencing using '
                             'standard LaTeX \\\u3164ref{...} syntax. The final reference '
                             'processing is happening on the published page, which can '
                             'be checked using "Preview" functionality.'),
                 max_length=50,
                 min_length=None,
                 validators=(),
                 form_classname='waggylabs-label',
                 **kwargs):
        super().__init__(required, help_text, max_length, min_length, validators, form_classname=form_classname, **kwargs)