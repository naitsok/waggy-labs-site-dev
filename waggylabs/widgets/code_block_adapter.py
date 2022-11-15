from django import forms
from django.conf import settings
from django.utils.functional import cached_property

from wagtail.blocks.struct_block import StructBlockAdapter
from wagtail.telepath import register

from waggylabs.blocks import CodeBlock, DEFAULT_CODEBLOCK_LANGS


DEFAULT_CODEMIRROR_VER = '5.65.9'

class CodeBlockAdapter(StructBlockAdapter):
    """Telepath adapter for the CodeBlock. According to
    https://docs.wagtail.org/en/stable/advanced_topics/customisation/streamfield_blocks.html#additional-javascript-on-structblock-forms.
    """
    
    js_constructor = 'waggylabs.blocks.CodeBlock'
    

    @cached_property
    def media(self):
        structblock_media = super().media
        codemirror_ver = settings.WAGGYLABS_CODEMIRROR_VER if hasattr(settings, 'WAGGYLABS_CODEMIRROR_VER') else DEFAULT_CODEMIRROR_VER
        codemirror_langs = settings.WAGGYLABS_CODEBLOCK_LANGS if hasattr(settings, 'WAGGYLABS_CODEBLOCK_LANGS') else DEFAULT_CODEBLOCK_LANGS
        codemirror_js = f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{codemirror_ver}/codemirror.min.js'
        codemirror_modes = list([f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{codemirror_ver}/mode/{mode[0]}/{mode[0]}.min.js' for mode in codemirror_langs])
        return forms.Media(
            js = structblock_media._js + [
                'waggylabs/js/blocks/code-block.js',
                codemirror_js,
                ] + codemirror_modes,
            css = {
                "all": (
                    f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{codemirror_ver}/codemirror.min.css',
                    'waggylabs/css/blocks/codemirror-tweaks.css',
                )
            }
        )

register(CodeBlockAdapter(), CodeBlock)
