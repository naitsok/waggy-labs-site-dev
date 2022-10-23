from django.utils.safestring import mark_safe

from wagtail import hooks


@hooks.register('insert_editor_js')
def editor_js():
    """Loads and initializes MathJax when Pages are edited in the Admin."""
    js_mathjax= (
        # below not needed for now as just using default MathJax inpu processor
        r"<script>window.MathJax = { tex: { tags: 'ams' } };</script>" + '\n'
        r'<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>' + '\n'
    )
    return mark_safe(js_mathjax)