import uuid

from django import template

register = template.Library()

@register.simple_tag(takes_context=False)
def random_uuid():
    """Django template tag to generate unique identifier
    needed for the HTML element ids, e.g. in Carousel block.

    Returns:
        str: unique identifier
    """
    return str(uuid.uuid4())


@register.simple_tag(takes_context=False)
def navbar_class(site_settings):
    """Generates CSS classes based on WaggyLabsSettings 
    for the <header> element containing navigation bar"""
    css_class = 'navbar navbar-expand-lg'
    if (not site_settings.theme_supports_color_mode
        and site_settings.navbar_theme):
        # if the upladed CSS theme does not support color modes,
        # add correct classes to have either light or dark navigation
        # bar dependinh on the navbar_theme setting
        css_class = (css_class +
                     ' navbar-' + site_settings.navbar_theme +
                     ' bg-' + site_settings.navbar_theme)
        
    if not site_settings.navbar_color:
        # if specific color has not been selected
        # add the default color and class
        # works only for Bootsrap 5.3 and higher
        # which has the bg-body-tertiary CSS class
        css_class = css_class + ' bg-body-tertiary'
        
    css_class = css_class + ' ' + site_settings.navbar_placement
    
    return css_class


@register.simple_tag(takes_context=False)
def main_class(site_settings, page):
    """Generates CSS class for the <main> element 
    depending on the WaggyLabsSettings and page sidebar."""
    
    if page.show_sidebar:
        if site_settings.content_width == 'narrow':
            return 'col-md-5 offset-md-2' # and col-md-3 for sidebar
        if site_settings.content_width == 'medium':
            return 'col-md-6 offset-md-1' # and col-md-4 for sidebar
        if site_settings.content_width == 'wide':
            return 'col-md-8' # and col-md-4 for sidebar
    
    if site_settings.content_width == 'narrow':
        return 'col-md-8 offset-md-2'
    if site_settings.content_width == 'medium':
        return 'col-md-10 offset-md-1'
    if site_settings.content_width == 'wide':
        return 'col-md-12'
    
    
@register.simple_tag(takes_context=False)
def sidebar_class(site_settings, page):
    """Generates CSS class for the sidebar <div> element
    depending on the WaggyLabsSettings and page sidebar."""
    css_class = ''
    if site_settings.content_width == 'narrow':
        css_class = 'col-md-3' # and col-md-3 for sidebar
    else:
        css_class = 'col-md-4'
    if not page.show_sidebar:
        css_class = css_class + ' d-none'
    return css_class
   