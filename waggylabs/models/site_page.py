from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin import widgets
from wagtail.admin.panels import FieldPanel, HelpPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock, PageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.search import index

# from wagtailmarkdown.blocks import MarkdownBlock

from wagtailmenus.models import MenuPageMixin
from wagtailmenus.panels import menupage_panel

from hitcount.models import HitCountMixin, HitCount
from hitcount.views import HitCountMixin as ViewHitCountMixin

from waggylabs.blocks.body import BodyBlock
from waggylabs.panels import ReadOnlyPanel


class SitePage(Page, MenuPageMixin, HitCountMixin):
    """A generic site page to contain content pages,
    such as Home, About, Research, Publications, etc.
    It can also list and filter posts if the site is used as a blog.
    """

    page_description = ('A generic site page to contain content, '
                        'such as Home, About, Research, Publications, etc. '
                        'It can also list and filter posts if the site is used as a blog.')
    template = 'waggylabs/pages/site_page.html'

    # Common fields

    show_in_menus_default = True

    # Database fields
    
    # Header image fields
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Image, that appears right after the title.')
    )
    show_header_image_on_page = models.BooleanField(
        blank=True,
        verbose_name=_('Show header image on page'),
        help_text=_('If true, the header image appears on top of the page '
                    'after the title. If false, header image is used only '
                    'situatively, e.g. when it appears in a list or a card '
                    'grid.')
    )
    # Content fields
    body = StreamField(
        BodyBlock(),
        use_json_field=True,
    )
    # Settings fields
    embed_caption_label = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Label for embeds'),
        help_text=_('For example, Embed. The label will be used to create '
                    'embed labels before caption. Leave empty for no label.'),
    )
    equation_caption_label = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Label for equations'),
        help_text=_('For example, Eqn. The label will be used to create '
                    'equatoion labels before caption. Note, that equation '
                    'labels are displayed only in preview dialogs. '
                    'Leave empty for no label.'),
    )
    figure_caption_label = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Label for figures'),
        help_text=_('For example, Figure. The label will be used to create '
                    'figure labels before caption. Leave empty for no label.'),
    )
    listing_caption_label = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Label for listings'),
        help_text=_('For example, Listing. The label will be used to create '
                    'listing labels before caption. Leave empty for no label.'),
    )
    table_caption_label = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Label for tables'),
        help_text=_('For example, Table. The label will be used to create '
                    'table labels before caption. Leave empty for no label.'),
    )

    # Search index configuration

    search_fields = Page.search_fields + [
        index.SearchField('body', partial_match=True, boost=2),
        index.AutocompleteField('body', boost=2),
        ]

    # Widgets for panels
  
    datetime_widget = widgets.AdminDateTimeInput(
        attrs={
            'placeholder': 'YYYY-MM-DDThh:mm'
        }
    )

    # Editor panels configuration

    content_panels = Page.content_panels + [
        HelpPanel(content=_('The Body field allows to build a complex page with different content. '
                            'Editing, however, does show the final look of the page on the site. '
                            'To see the final version, use the "Preview" functionality below. '
                            'There are different blocks of the Body that can be used. '
                            'Heading block allows to set a heading of the certain level. '
                            'Paragraph is a simple rich text block that allows to interactively '
                            'make links to other site Pages, upload images and documents. '
                            'Note that images added in the block will not show in side panel '
                            'and will have nor caption nor reference. '),
                  heading=_('Tips for editing the Body field'),
                  classname='title'),
        FieldPanel('body'),
        ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel(
            [
                FieldPanel('header_image'),
                FieldPanel('show_header_image_on_page'),
            ],
            heading=_('Header image')
        ),  
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel,
        # MultiFieldPanel(
        #     [
        #         FieldPanel('show_search'),
        #         FieldPanel('show_tag_cloud'),
        #         FieldPanel('show_categories'),
        #     ],
        #     heading=_('Page settings')
        # ),
        MultiFieldPanel(
            [
                FieldPanel('embed_caption_label'),
                FieldPanel('equation_caption_label'),
                FieldPanel('figure_caption_label'),
                FieldPanel('listing_caption_label'),
                FieldPanel('table_caption_label'),
            ],
            heading=_('Label settings'),
        ),
        MultiFieldPanel(
            [
                ReadOnlyPanel('first_published_at', heading='First published at'),
                ReadOnlyPanel('last_published_at', heading='Last published at'),
                ReadOnlyPanel('hit_counts', heading='Number of views'),
            ],
            heading=_('General information'),
        ),
    ]
    
    # Parent page / subpage type rules
    
    # parent_page_types = ['waggylabs.SitePage'] # 'main.HomePage', 
    # parent_page_types = []
    subpage_types = ['waggylabs.SitePage'] #, 'main.FormPage']

    # Methods
    
    @classmethod
    def _check_cite_block(cls, block):
        """Internal method to check the block is one that gets cited."""
        return (block.block_type == 'citation' 
                or block.block_type == 'document')
    
    @classmethod
    def _get_cite_blocks(cls, stream_block):
        """Internal method to get all citation blocks
        within a StreamBlock"""
        cite_blocks = []
        for block in stream_block:
            if (block.block_type == 'citation' 
                or block.block_type == 'document'):
                cite_blocks.append(block)
        return cite_blocks
    
    @classmethod
    def _get_cite_blocks_from_accordion(cls, accordion_block):
        """Gets citation and document blocks located inside of
        AccordionBlock."""
        cite_blocks = []
        for accordion_item in accordion_block.value['items']:
            for acc_item_block in accordion_item['body']:
                if SitePage._check_cite_block(acc_item_block):
                    cite_blocks.append(acc_item_block)
        return cite_blocks
    
    @classmethod
    def _get_cite_blocks_from_columns(cls, columns_block):
        """Gets citation and document blocks located inside of
        ColumnsBlock."""
        cite_blocks = []
        for columns_item in columns_block.value['items']:
            for col_item_block in columns_item['body']:
                if SitePage._check_cite_block(col_item_block):
                    cite_blocks.append(col_item_block)
                if col_item_block.block_type == 'accordion':
                    cite_blocks = (cite_blocks +
                                   SitePage._get_cite_blocks_from_accordion(col_item_block))
        return cite_blocks
    
    
    def citation_blocks(self):
        """Returns citations and documents found in body StreamField and
        its sub blocks."""   
        return BodyBlock.citation_blocks(self.body)
            

    def hit_counts(self):
        """Displays hitcounts for the page if it has been created."""
        if self.pk is not None:
            # the page is created and hitcounts make sense
            return self.hit_count.hits
        else:
            return 0

    def serve(self, request, *args, **kwargs):
        hit_count = HitCount.objects.get_for_object(self)
        ViewHitCountMixin.hit_count(request, hit_count)
        return super().serve(request, *args, **kwargs)