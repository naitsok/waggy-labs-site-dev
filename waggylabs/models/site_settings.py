from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey, ForeignKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, HelpPanel, ObjectList, TabbedInterface, InlinePanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.models import Orderable


class SocialLink(models.Model):
    """Class to contain all the information for one social link."""
    title = models.CharField(
        max_length=255,
        blank=False,
        help_text=_('Title of the social network. For example, Instagram.'),
        verbose_name=_('Title of the social network.')
    )
    username = models.CharField(
        max_length=255,
        blank=False,
        help_text=_('Username for the social network.'),
        verbose_name=_('Username for the social network')
    )
    username_prefix = models.CharField(
        max_length=10,
        blank=True,
        help_text=_('Additional prefix before the username if display username is selects. For example "@" for Twitter.'),
        verbose_name=_('Prefix for the username')
    )
    icon = models.CharField(
        max_length=255,
        blank=True,
        help_text=_('Icon name from Font Awesome website. If left blank, title will used.'),
        verbose_name=_('Icon name from Font Awesome website')
    )
    domain = models.CharField(
        max_length=10,
        blank=True,
        help_text=_('Domain name for the social network. If left blank, "com" will be used.'),
        verbose_name=_('Domain name for the social network')
    )
    class SocialLinkText(models.TextChoices):
        """Defines how to show the text in for the social network links."""
        ICON = 'icon', _('Only social netwok icon')
        TITLE = 'title', _('Title of the social network')
        USERNAME = 'username', _('Username in the social network')
    link_text = models.CharField(
        max_length=10,
        blank=False,
        choices=SocialLinkText.choices,
        default=SocialLinkText.ICON,
        help_text=_('Choose how to display URLs to the social networks: only icons of the networks, '
                    'icons and network titles or icons and usernames in the networks. Note that some icons may '
                    'not be available according to the network title. Please check Font Awesome Icons for icon '
                    'availability.'),
        verbose_name=_('Social network display text')
    )
    
    panels = [
        FieldPanel('title'),
        FieldPanel('username'),
        FieldPanel('username_prefix'),
        FieldPanel('icon'),
        FieldPanel('domain'),
        FieldPanel('link_text')
    ]
    
    class Meta:
        abstract = True
    
    
class WaggyLabsSettingsSocialLinks(Orderable, SocialLink):
    """Class that connects SocialLink with Waggy Labs Settings model."""
    page = ParentalKey('waggylabs.WaggyLabsSettings', on_delete=models.CASCADE, related_name='social_links')


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
        help_text=_('CSS file with theme to be used instead of default Bootstrap theme. See Bootstrap documentation.'),
        verbose_name=_('Bootstrap CSS theme'),
    )
    class NavbarPlacement(models.TextChoices):
        """Navbar placement choices from the Bootstrap documentation: default, sticky-top or fixed-top"""
        DEFAULT = '', _('Default')
        STICKY_TOP = 'sticky-top', _('Sticky top')
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
        HelpPanel(content=_('Choose the Bootstrap theme for your site and upload the Bootstrap CSS file to be used '
                            'istead of default one. Select the correct navigation bar theme according to the chosen CSS file. '
                            'Select the desired placement of the navigation bar. See Bootstrap documentation.'),
                  heading=_('Explanation of the settings'),
                  classname='title'),
        FieldPanel('site_theme'),
        FieldPanel('navbar_theme'),
        FieldPanel('navbar_placement'),
        FieldPanel('navbar_menu_alignment')
    ]
    
    social_panels = [
        HelpPanel(content=_('Enter your social network account usernames. Do not enter full URLs.'),
                  heading=_('Explanation of the settings'),
                  classname='title'),
        InlinePanel('social_links', label='Social links')
    ]
    
    edit_handler = TabbedInterface([
        ObjectList(site_name_panels, heading=_('Site name settings')),
        ObjectList(theme_panels, heading=_('Theme settings')),
        ObjectList(social_panels, heading=_('Social links'))
    ])
    
    class Meta:
        verbose_name = _('Site Settings')