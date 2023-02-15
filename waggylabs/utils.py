import re


RE_LABEL = re.compile(r'\\label\{(.*?)\}', re.IGNORECASE)
RE_REF = re.compile(r'\\ref\{(.*?)\}', re.IGNORECASE)
RE_EQREF = re.compile(r'\\eqref\{(.*?)\}', re.IGNORECASE)
RE_CITE = re.compile(r'\\cite\{(.*?)\}', re.IGNORECASE)
def pk_to_markdown(value, pk):
    """Modifies all label, ref, eqref, cite with page primary key
    to avoid collisions when multiple parts from different pages are rendered
    on one page (e.g. when pages are renedered in list)."""
    pk = str(pk)
    value = re.sub(RE_LABEL,
                   lambda m: (r'\label{' + m.group(1) + '-' + pk + '}'),
                   value)
    value = re.sub(RE_REF,
                   lambda m: (r'\ref{' + m.group(1) + '-' + pk + '}'),
                   value)
    value = re.sub(RE_EQREF,
                   lambda m: (r'\eqref{' + m.group(1) + '-' + pk + '}'),
                   value)
    value = re.sub(RE_CITE,
                   lambda m: (
                       r'\cite{' +
                       ','.join([cite + '-' + pk for cite in m.group(1).split(',')]) + '}'
                    ),
                   value)
    return value