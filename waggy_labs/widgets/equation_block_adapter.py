from django import forms
from django.conf import settings
from django.utils.functional import cached_property

from wagtail.blocks.struct_block import StructBlockAdapter
from wagtail.telepath import register

from waggy_labs.blocks import EquationBlock


DEFAULT_CODEMIRROR_VER = '5.65.9'

class EquationBlockAdapter(StructBlockAdapter):
    """Telepath adapter for the EquationBlock. According to
    https://docs.wagtail.org/en/stable/advanced_topics/customisation/streamfield_blocks.html#additional-javascript-on-structblock-forms.
    """
    js_constructor = 'waggy_labs.blocks.EquationBlock'
    

    @cached_property
    def media(self):
        structblock_media = super().media
        codemirror_ver = settings.WAGGYLABS_CODEMIRROR_VER if hasattr(settings, 'WAGGYLABS_CODEMIRROR_VER') else DEFAULT_CODEMIRROR_VER
        codemirror_js = f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{codemirror_ver}/codemirror.min.js'
        codemirror_modes = [f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{codemirror_ver}/mode/stex/stex.min.js']
        return forms.Media(
            js = structblock_media._js + [
                'waggy_labs/js/blocks/equation-block.js',
                codemirror_js,
                ] + codemirror_modes,
            css = {
                "all": (
                    f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{codemirror_ver}/codemirror.min.css',
                    'waggy_labs/css/blocks/codemirror.tweaks.css',
                )
            }
        )

register(EquationBlockAdapter(), EquationBlock)
