from django import forms
from django.conf import settings
from django.utils.functional import cached_property

from wagtail.blocks.struct_block import StructBlockAdapter
from wagtail.telepath import register

from waggylabs.blocks.code import CodeBlock, CODEBLOCK_LANGS


CODEMIRROR_VERSION = getattr(settings, 'WAGGYLABS_CODEMIRROR_VERSION', '5.65.9')
CODEBLOCK_LANGS = getattr(settings, 'WAGGYLABS_CODEBLOCK_LANGS', CODEBLOCK_LANGS)
CODEBLOCK_LANGS = list(
    [
        f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/mode/{mode[0]}/{mode[0]}.min.js' 
        for mode in CODEBLOCK_LANGS
    ]
)

class CodeBlockAdapter(StructBlockAdapter):
    """Telepath adapter for the CodeBlock. According to
    https://docs.wagtail.org/en/stable/advanced_topics/customisation/streamfield_blocks.html#additional-javascript-on-structblock-forms.
    """
    
    js_constructor = 'waggylabs.blocks.CodeBlock'
    

    @cached_property
    def media(self):
        structblock_media = super().media
        return forms.Media(
            js = structblock_media._js + [
                'waggylabs/js/blocks/code-adapter.js',
                f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/codemirror.min.js',
                ] + CODEBLOCK_LANGS,
            css = {
                "all": (
                    f'https://cdnjs.cloudflare.com/ajax/libs/codemirror/{CODEMIRROR_VERSION}/codemirror.min.css',
                    'waggylabs/css/blocks/codemirror-tweaks.css',
                )
            }
        )

register(CodeBlockAdapter(), CodeBlock)
