import html

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern, InlineProcessor, SimpleTagInlineProcessor

RE_BEGIN = r'\\begin{(.*?)}([\s\S]*?)\\end{\1}'
RE_INLINE = r'()\\\\\[+([^$\n]+?)\\\\\]+'
# RE_INLINE = r'()\$\$([^\$\n]+?)\$\$'


class BeginMathJaxPattern(Pattern):
    def handleMatch(self, m):
        return m.group(3)
    

class InlineMathJaxPattern(Pattern):
    def handleMatch(self, m):
        return m.group(2)

class MathJaxPattern(Pattern):
    def __init__(self, md):
        Pattern.__init__(self, r'\\begin{(.*?)}([\s\S]*?)\\end{\1}', md)

    def handleMatch(self, m, data):
        # Pass the math code through, unmodified except for basic entity substitutions.
        # Stored in htmlStash so it doesn't get further processed by Markdown.
        text = html.escape(m.group(2) + m.group(3) + m.group(2))
        return self.markdown.htmlStash.store(text)


class MathJaxExtension(Extension):
    def extendMarkdown(self, md):
        # Needs to come before escape matching because \ is pretty important in LaTeX
        # md.inlinePatterns.add('mathjax', MathJaxPattern(md), '<escape')
        md.inlinePatterns.register(SimpleTagInlineProcessor(RE_INLINE, 's'), 'begin', 172)


def makeExtension(configs={}):
    return MathJaxExtension(**configs)