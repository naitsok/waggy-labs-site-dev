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
def navbar_style(site_settings):
    """Generates style property based on the WaggyLabsSettings
    for the <header> element containing navigation bar"""
    style = ''
    if site_settings.navbar_color:
        style = f'background: {site_settings.navbar_color};'
        if site_settings.navbar_theme == 'light':
            style = f'{style} filter: brightness(120%);'
        if site_settings.navbar_theme == 'dark':
            style = f'{style} filter: brightness(80%);'
            
    return style