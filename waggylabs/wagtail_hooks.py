from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from wagtail import hooks


@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('waggylabs/css/admin-styles.css')
    )


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('waggylabs/css/editor-styles.css')
    )
    

@hooks.register('insert_global_admin_js')
def global_editor_js():
    """Loads and initializes MathJax when Pages are edited in the Admin."""
    mathjax_js= (
        # below not needed for now as just using default MathJax inpu processor
        """<script>
        window.MathJax = {
            loader: {
                load: ['[tex]/autoload'],
            },
            tex: {
                packages: {"[+]": ["autoload"]},
                tags: "ams",
                inlineMath: [["\\\\(", "\\\\)"]],
            },
        };
        </script>\n
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>\n"""
    )
    return mark_safe(mathjax_js)