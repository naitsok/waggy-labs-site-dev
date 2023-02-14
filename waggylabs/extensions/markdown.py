
import html
import re
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor, SimpleTagInlineProcessor
from markdown.postprocessors import Postprocessor
from markdown.preprocessors import Preprocessor
from markdown.util import AtomicString


RE_LABEL = re.compile(r'\\label\{(.*?)\}', re.IGNORECASE)
RE_REF = re.compile(r'\\ref\{(.*?)\}', re.IGNORECASE)
RE_EQREF = re.compile(r'\\eqref\{(.*?)\}', re.IGNORECASE)
RE_CITE = re.compile(r'\\cite\{(.*?)\}', re.IGNORECASE)
def page_pk_to_markdown(value: str, pk: int):
    """Modifies all label, ref, eqref, cite ids with page primary key
    to avoid collisions when multiple parts from different pages are rendered
    on one page (e.g. when pages are renedered in list)."""
    value = re.sub(RE_LABEL,
                   lambda m: (r'\label{' + m.group(1) + '-' + str(pk) + '}'),
                   value)
    value = re.sub(RE_REF,
                   lambda m: (r'\ref{' + m.group(1) + '-' + str(pk) + '}'),
                   value)
    value = re.sub(RE_EQREF,
                   lambda m: (r'\eqref{' + m.group(1) + '-' + str(pk) + '}'),
                   value)
    value = re.sub(RE_CITE,
                   lambda m: (
                       r'\cite{' +
                       ','.join([cite + '-' + str(pk) for cite in m.group(1).split(',')]) + '}'
                    ),
                   value)
    return value


class DollarSignPreprocessor(Preprocessor):
    """Preprocessor to replace \$ symbol with '{{DOLLAR}}' to avoid its determination as LaTeX equation."""
    def run(self, lines):
        new_lines = []
        for line in lines:
            new_lines.append(line.replace('\\$', '{{DOLLAR}}'))
        return new_lines


class DollarSignPostprocessor(Postprocessor):
    """Posprocessor to return $ signs back from {{DOLLAR}}."""
    def run(self, text):
        return text.replace('{{DOLLAR}}', '$')


class StrikethroughExtension(Extension):
    """Extenstion for ~~strikethrough~~ pattern."""
    def extendMarkdown(self, md):
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()~~(.*?)~~', 's'), 's', 171)


RE_INLINE = r'()\\\\\(+([^$\n]+?)\\\\\)+'
RE_INLINE2 = r'()\$+([^$\n]+?)\$+'
class MathJaxInlineProcessor(InlineProcessor):
    """Processor for MathJax inline equations in Python-Markdown."""
    def handleMatch(self, m, data):
        # Pass the math code through, unmodified except for basic entity substitutions.
        # Mark as Atomic String in order to prevent further processing.
        el = etree.Element('span')
        el.text = AtomicString(html.escape('\\(' + m.group(2).replace('\n', '') + '\\)'))
        return el, m.start(0), m.end(0)


RE_BLOCK = r'()\\\\\[+([\s\S]+?)\\\\\]+'
class MathJaxBlockProcessor(InlineProcessor):
    """Processor for MathJax block equations in Python-Markdown."""
    def handleMatch(self, m, data):
        # Pass the math code through, unmodified except for basic entity substitutions.
        # Mark as Atomic String in order to prevent further processing.
        el = etree.Element('p')
        el.text = AtomicString(html.escape('\\[' + m.group(2).replace('\n', '') + '\\]'))
        return el, m.start(0), m.end(0)


RE_BEGIN = r'\\begin{(.*?)}([\s\S]*?)\\end{\1}'
class MathJaxBeginProcessor(InlineProcessor):
    """Processor for MathJax equations entered using \\begin{...}...\\end{...} pattern."""
    def handleMatch(self, m, data):
        # Pass the math code through, unmodified except for basic entity substitutions.
        # Mark as Atomic String in order to prevent further processing.
        el = etree.Element('p')
        el.text = AtomicString(html.escape('\\begin{' + m.group(1) + '}' + m.group(2).replace('\n', '') + '\\end{' + m.group(1) + '}'))
        return el, m.start(0), m.end(0)
    

class WaggyLabsMarkdownExtenstion(Extension):
    """Registers all the extensions for Python-Markdown."""
    def extendMarkdown(self, md):
        # Prepocessors
        md.preprocessors.register(DollarSignPreprocessor(), 'dollar-pre', 19)
        # MathJax equations, must go before escaping.
        md.inlinePatterns.register(MathJaxInlineProcessor(RE_INLINE), 'math-inline', 185)
        md.inlinePatterns.register(MathJaxInlineProcessor(RE_INLINE2), 'math-inline', 186)
        md.inlinePatterns.register(MathJaxBlockProcessor(RE_BLOCK), 'math-block', 187)
        md.inlinePatterns.register(MathJaxBeginProcessor(RE_BEGIN), 'math-begin', 189)
        # ~~strikethrough~~ pattern.
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()~~(.*?)~~', 's'), 's', 171)
        # Postprocessors
        md.postprocessors.register(DollarSignPostprocessor(), 'dollar-post', 19)
        
        
def makeExtension(configs={}):
    return WaggyLabsMarkdownExtenstion(**configs)