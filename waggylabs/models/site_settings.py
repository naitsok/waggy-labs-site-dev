from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.panels import FieldPanel, HelpPanel, ObjectList, TabbedInterface, InlinePanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.models import Orderable

from waggylabs.widgets import IconInput


class SiteLink(models.Model):
    """Class to add links on the navbar. For example, links
    to social websites."""
    link = models.URLField(
        max_length=255,
        blank=False,
        help_text=_('Full URL to the website'),
        verbose_name=_('Link to the website'),
    )
    text = models.CharField(
        max_length=255,
        blank=True,
        help_text=_('Text for the link to be displayed. Can be empty '
                    ' if only the icon to be displayed,'),
        verbose_name=_('Text of the link'),
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('Icon for the link. Can be empty if no icon '
                    'to be displayed.'),
        verbose_name=_('Link icon'),
    )
    style = models.CharField(
        max_length=50,
        blank=False,
        choices=[
            ('btn btn-primary', _('Button primary')),
            ('btn btn-secondary', _('Button secondary')),
            ('btn btn-success', _('Button success')),
            ('btn btn-danger', _('Button danger')),
            ('btn btn-warning', _('Button warning')),
            ('btn btn-info', _('Button info')),
            ('btn btn-outline-primary', _('Button outline primary')),
            ('btn btn-outline-secondary', _('Button outline secondary')),
            ('btn btn-outline-success', _('Button outline success')),
            ('btn btn-outline-danger', _('Button outline danger')),
            ('btn btn-outline-warning', _('Button outline warning')),
            ('btn btn-outline-info', _('Button outline info')),
            ('nav-link', _('Link')),
            ('nav-link active', _('Link active')),
        ],
        help_text=_('Select the style for the link. See '
                    'Bootstrap documentation.'),
        verbose_name=_('Link style'),
    )
    
    panels = [
        FieldPanel('link'),
        FieldPanel('text'),
        FieldPanel('icon', widget=IconInput),
        FieldPanel('style'),
    ]
    
    class Meta:
        abstract = True
    
    
class WaggyLabsSettingsSiteLinks(Orderable, SiteLink):
    """Class that connects SiteLink with Waggy Labs Settings model."""
    page = ParentalKey('waggylabs.WaggyLabsSettings', on_delete=models.CASCADE, related_name='site_links')


@register_setting
class WaggyLabsSettings(BaseSiteSetting, ClusterableModel):
    """Settings for Waggy Labs site to set navbar (or small brand) image, 
    navbar (brand) slogan, and controls if the Waggy Labs site name should appear in the navbar."""
    
    # Database fields
    # Settings related to the site name display
    site_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Image that appears in navigation bar and in the browser tab.'),
        verbose_name=_('Navigation bar and browser tab image'),
    )
    site_slogan = models.CharField(
        max_length=255,
        blank=True,
        help_text=_('Phrase, that appears in navbar on the right to the brand image.'),
        verbose_name=_('Slogan'),
    )
    show_site_name = models.BooleanField(
        default=True,
        help_text=_('Indicates if title of the Waggy Labs site appears in navigation bar and in browser tab e.g., Page Title - Site Name.'),
        verbose_name=_('Show site name in navigation bar and browser tab'),
    )
    site_name_separator = models.CharField(
        max_length=10,
        blank=True,
        help_text=_('Separator for site name e.g., Page Title - Site Name or Page Title : Site Name.'),
        verbose_name=_('Separator for the site name'),
    )
    class SiteNameAlignment(models.TextChoices):
        """Alignment choices for the site name in navbar: before page title or after page title."""
        LEFT = 'L', _('Before page title')
        RIGHT = 'R', _('After page title')
    site_name_alignment = models.CharField(
        max_length=1,
        choices=SiteNameAlignment.choices,
        default=SiteNameAlignment.RIGHT,
        help_text=_('The alignment of site name: before or after page title.'),
    )
    
    # Settings related to themes and navigation bar customization
    site_theme = models.FileField(
        blank=True,
        help_text=_('CSS file with theme to be used instead of default Bootstrap theme.'),
        verbose_name=_('Bootstrap CSS theme'),
    )
    # theme_supports_color_modes = models.BooleanField(
    #     blank=True,
    #     help_text=_('If the CSS theme file suppots Bootstrap dark and light modes.'),
    #     verbose_name=_('CSS theme supporst dark and light modes'),
    # )
    class NavbarPlacement(models.TextChoices):
        """Navbar placement choices from the Bootstrap documentation: default, sticky-top or fixed-top"""
        DEFAULT = '', _('Default')
        STICKY_TOP = 'sticky-top', _('Sticky top')
        FIXED_TOP = 'fixed-top', _('Fixed top')
    navbar_placement = models.CharField(
        max_length=10,
        choices=NavbarPlacement.choices,
        default=NavbarPlacement.DEFAULT,
        blank=True,
        help_text=_('Navigation bar placement options: default, sticky-top or fixed-top. See Bootstrap documentation.')
    )
    class NavbarTheme(models.TextChoices):
        """Navigation bar theme: dark or light. Correct choice needs to be selected based on the selected CSS Bootstrap theme."""
        LIGHT = '', _('Light')
        PRIMARY = 'primary', _('Primary')
        DARK = 'dark', _('Dark')
    navbar_theme = models.CharField(
        max_length=25,
        choices=NavbarTheme.choices,
        default=NavbarTheme.LIGHT,
        blank=True,
        help_text=_('Navigation bar theme: dark or light. Choice depends on the choice of the CSS Bootstrap theme.')
    )
    class NavbarMenuAlignment(models.TextChoices):
        """Alignment of the menu in the navigation bar."""
        LEFT = '', _('Left')
        RIGHT = 'ms-md-auto', _('Right')
    navbar_menu_alignment = models.CharField(
        max_length=10,
        choices=NavbarMenuAlignment.choices,
        default=NavbarMenuAlignment.LEFT,
        blank=True,
        help_text=_('Menu links alignment in the navigation bar.')
    )

    # Panels for the Wagtail admin
    site_name_panels = [
        HelpPanel(content=_('Edit settings for the currently selected Waggy Labs site'),
                  heading=_('Explanation of the settings'),
                  classname='title'),
        FieldPanel('site_icon'),
        FieldPanel('site_slogan'),
        FieldPanel('show_site_name'),
        FieldPanel('site_name_separator'),
        FieldPanel('site_name_alignment')
    ]
    
    theme_panels = [
        HelpPanel(content=_('Choose the Bootstrap theme for your site and upload the '
                            'Bootstrap CSS file to be used istead of default one. Select '
                            'the correct navigation bar theme according to the '
                            'chosen CSS file. Select the desired placement of the '
                            'navigation bar. See Bootstrap documentation.'),
                  heading=_('Explanation of the settings'),
                  classname='title'),
        FieldPanel('site_theme'),
        FieldPanel('navbar_theme'),
        FieldPanel('navbar_placement'),
        FieldPanel('navbar_menu_alignment')
    ]
    
    social_panels = [
        HelpPanel(content=_('Links to the external websites can contain icon, text, or icon and text.'),
                  heading=_('Explanation of the settings'),
                  classname='title'),
        InlinePanel('site_links', label='Links to external sites')
    ]
    
    edit_handler = TabbedInterface([
        ObjectList(site_name_panels, heading=_('Site name settings')),
        ObjectList(theme_panels, heading=_('Theme settings')),
        ObjectList(social_panels, heading=_('External links'))
    ])
    
    class Meta:
        verbose_name = _('Site Settings')