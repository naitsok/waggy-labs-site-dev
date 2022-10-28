import html
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.util import AtomicString


RE_INLINE = r'()\\\\\(+([\s\S]+?)\\\\\)+'
RE_BLOCK = r'()\\\\\[+([\s\S]+?)\\\\\]+'
RE_BEGIN = r'\\begin{(.*?)}([\s\S]*?)\\end{\1}'


class MathJaxBeginProcessor(InlineProcessor):

    def handleMatch(self, m, data):
        # Pass the math code through, unmodified except for basic entity substitutions.
        # Stored in htmlStash so it doesn't get further processed by Markdown.
        el = etree.Element('div')
        el.text = AtomicString(html.escape('\\begin{' + m.group(1) + '}' + m.group(2).replace('\n', '') + '\\end{' + m.group(1) + '}'))
        return el, m.start(0), m.end(0)
    
class MathJaxBracketProcessor(InlineProcessor):

    def handleMatch(self, m, data):
        # Pass the math code through, unmodified except for basic entity substitutions.
        # Stored in htmlStash so it doesn't get further processed by Markdown.
        el = etree.Element('span')
        el.text = AtomicString(html.escape('\\(' + m.group(2).replace('\n', '') + '\\)'))
        return el, m.start(0), m.end(0)


class MathJaxExtension(Extension):
    def extendMarkdown(self, md):
        # Needs to come before escape matching because \ is pretty important in LaTeX
        md.inlinePatterns.register(MathJaxBracketProcessor(RE_INLINE), 'math-inline', 189)
        md.inlinePatterns.register(MathJaxBracketProcessor(RE_BLOCK), 'math-block', 188)
        md.inlinePatterns.register(MathJaxBeginProcessor(RE_BEGIN), 'math-begin', 187)


def makeExtension(configs={}):
    return MathJaxExtension(**configs)