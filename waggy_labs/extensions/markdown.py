from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor

class StrikethroughExtension(Extension):
    """Extenstion for ~~strikethrough~~ pattern."""
    def extendMarkdown(self, md):
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()~~(.*?)~~', 's'), 's', 175)
        
        
def makeExtension(configs={}):
    return StrikethroughExtension(**configs)