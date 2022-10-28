import markdown
import html

RE_BEGIN = r'\\begin{(.*?)}([\s\S]*?)\\end{\1}'
RE_INLINE = r'()\\\\\[+([^$\n]+?)\\\\\]+'

s =  'The reference for a super wise [quote](#quote-1). And referencing [figure](#figure-1).\r\nSome great inline equation \\\\[ \\frac{1}{2} \\\\ \\frac{1}{2} \\\\].\r\n\r\n$$ Block\\, \\\\ Math $$\r\n\r\nA reference to an equation \\eqref{eqn:sample}. $\\frac{1}{2} \\\\ \\frac{1}{2}$.\r\n\r\n\\begin{align}\r\nA & = \\int_0^\\infty \\frac{x^3}{e^x-1}\\,dx \\\\\r\n& = \\frac{\\pi^4}{15}\r\n\\label{eqn:sample}\r\n\\end{align}\r\n\r\n```latex\r\n\\begin{equation}\r\n\\omega_p\r\n\\end{equation}\r\n```\r\n\\begin{bmatrix}\r\nA & B \\\\\r\nC & D\r\n\\label{eqn:sample2}\r\n\\end{bmatrix}\r\nmore text more and more text writing.\r\n\r\n```python\r\ndef field(self):\r\n        field_kwargs = {"widget": MyMarkdownTextarea(attrs={"rows": self.rows})}\r\n        field_kwargs.update(self.field_options)\r\n        return forms.CharField(**field_kwargs)\r\n```'

class InlineMathJaxProcessor(markdown.inlinepatterns.InlineProcessor):
    def handleMatch(self, m, data):
        print(m.group(2))
        text = html.escape('\\begin{' + m.group(1) + '}'+ m.group(2).strip() + '\\end{' + m.group(1) + '}\n')
        return text, m.start(0), m.end(0)
    
class MyExtension(markdown.extensions.Extension):
    def extendMarkdown(self, md):
        ext = InlineMathJaxProcessor(RE_BEGIN)
        print(ext.getCompiledRegExp())
        md.inlinePatterns.register(ext, 'eqn', 189)
        
print(markdown.markdown(s, extensions=[MyExtension()]))