# Generated by Django 4.1.3 on 2022-12-01 13:14

from django.db import migrations
import waggylabs.blocks.carousel
import waggylabs.blocks.label
import waggylabs.blocks.mathjax_markdown
import waggylabs.blocks.table
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('waggylabs', '0011_alter_sitepage_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitepage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full subtitle', required=True)), ('blockquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.TextBlock(label='Quote text.', required=True, rows=3)), ('author', wagtail.blocks.CharBlock(label='Author of the quoted text.', required=False)), ('source', wagtail.blocks.CharBlock(label='Source of the quoted text.', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-blockquote', max_length=50, required=False))])), ('pages', wagtail.blocks.PageChooserBlock(can_choose_root=True, required=True)), ('embed', wagtail.embeds.blocks.EmbedBlock(required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True)), ('markdown', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(icon='doc-full', required=True)), ('code', wagtail.blocks.StructBlock([('code', wagtail.blocks.StructBlock([('mode', wagtail.blocks.ChoiceBlock(choices=[('python', 'Python'), ('clike', 'C, C++, C#'), ('clike', 'Java'), ('javascript', 'Javascript'), ('xml', 'HTML, XML'), ('octave', 'MATLAB'), ('mathematica', 'Mathematica'), ('r', 'R'), ('clike', 'Kotlin'), ('swift', 'Swift'), ('powershell', 'Powershell'), ('sql', 'SQL'), ('css', 'CSS')], label='Code language')), ('code', wagtail.blocks.TextBlock(label='Code snippet', required=True, rows=4))], label=None)), ('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Listing caption', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-listing', max_length=50, required=False))])), ('figure', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Graphic', required=True)), ('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Figure caption', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-figure', max_length=50, required=False))])), ('equation', wagtail.blocks.StructBlock([('equation', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='150px', easymde_min_height='150px', easymde_status='false', easymde_toolbar_config='subscript,superscript,equation,matrix,align,multiline,split,gather,alignat,flalign,|,preview,side-by-side,fullscreen', help_text='Write or paste LaTeX style equation (equation, matrix, align, etc. environments are supported).', required=True)), ('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Equation caption', required=False)), ('label', waggylabs.blocks.label.LabelBlock(max_length=50, required=False))])), ('carousel', waggylabs.blocks.carousel.ImageCarouselBlock()), ('table_figure', wagtail.blocks.StructBlock([('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='150px', easymde_min_height='150px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Table caption', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Table image', required=True)), ('footer', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Table footer', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-table', max_length=50, required=False))])), ('table', wagtail.blocks.StructBlock([('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Table caption', required=False)), ('table', waggylabs.blocks.table.BareTableBlock(help_text='Columns and rows can be added via context menu appearing on the right click. Markdown inside cells is supported. Inline LateX equations can be added using $...$ pattern.', keep_table_tag=False, label='Table data', required=True)), ('footer', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Table footer', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-table', max_length=50, required=False))])), ('accordion', wagtail.blocks.StructBlock([('style', wagtail.blocks.ChoiceBlock(choices=[('collapsible', 'Items collapse'), ('stays_open', 'Items stay open')], label='Collapse items when new items opens or keep them open')), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(form_classname='full subtitle', label='Item Heading', required=True)), ('body', wagtail.blocks.StreamBlock([('markdown', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='150px', easymde_min_height='150px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text='', required=False)), ('code', wagtail.blocks.StructBlock([('code', wagtail.blocks.StructBlock([('mode', wagtail.blocks.ChoiceBlock(choices=[('python', 'Python'), ('clike', 'C, C++, C#'), ('clike', 'Java'), ('javascript', 'Javascript'), ('xml', 'HTML, XML'), ('octave', 'MATLAB'), ('mathematica', 'Mathematica'), ('r', 'R'), ('clike', 'Kotlin'), ('swift', 'Swift'), ('powershell', 'Powershell'), ('sql', 'SQL'), ('css', 'CSS')], label='Code language')), ('code', wagtail.blocks.TextBlock(label='Code snippet', required=True, rows=4))], label=None)), ('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Listing caption', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-listing', max_length=50, required=False))])), ('figure', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Graphic', required=True)), ('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Figure caption', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-figure', max_length=50, required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(required=True)), ('equation', wagtail.blocks.StructBlock([('equation', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='150px', easymde_min_height='150px', easymde_status='false', easymde_toolbar_config='subscript,superscript,equation,matrix,align,multiline,split,gather,alignat,flalign,|,preview,side-by-side,fullscreen', help_text='Write or paste LaTeX style equation (equation, matrix, align, etc. environments are supported).', required=True)), ('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Equation caption', required=False)), ('label', waggylabs.blocks.label.LabelBlock(max_length=50, required=False))])), ('table_figure', wagtail.blocks.StructBlock([('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='150px', easymde_min_height='150px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Table caption', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Table image', required=True)), ('footer', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Table footer', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-table', max_length=50, required=False))])), ('table', wagtail.blocks.StructBlock([('caption', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Table caption', required=False)), ('table', waggylabs.blocks.table.BareTableBlock(help_text='Columns and rows can be added via context menu appearing on the right click. Markdown inside cells is supported. Inline LateX equations can be added using $...$ pattern.', keep_table_tag=False, label='Table data', required=True)), ('footer', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, label='Table footer', required=False)), ('label', waggylabs.blocks.label.LabelBlock(form_classname='waggylabs-label-table', max_length=50, required=False))]))], required=True))])))])), ('card_grid', wagtail.blocks.StructBlock([('equal_height', wagtail.blocks.ChoiceBlock(choices=[('equal', 'Equal'), ('not_equal', 'Wrap content')], label='Height')), ('style', wagtail.blocks.ChoiceBlock(choices=[('separate', 'Separate'), ('grouped', 'Grouped')], label='Grouping')), ('orientation', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'Vertical'), ('horizontal', 'Horizontal')], label='Orientation')), ('columns', wagtail.blocks.ChoiceBlock(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], label='Number of columns')), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', waggylabs.blocks.mathjax_markdown.MathJaxMarkdownBlock(easymde_combine='true', easymde_max_height='100px', easymde_min_height='100px', easymde_status='false', easymde_toolbar_config='bold,italic,strikethrough,|,unordered-list,ordered-list,link,|,code,subscript,superscript,|,preview,side-by-side,fullscreen,guide', help_text=None, required=False)), ('links', wagtail.blocks.StreamBlock([('external_link', wagtail.blocks.StructBlock([('link', wagtail.blocks.URLBlock(label='Link to external site', required=True)), ('text', wagtail.blocks.CharBlock(label='Text of the link', required=True)), ('style', wagtail.blocks.ChoiceBlock(choices=[('', 'Choose style'), ('btn btn-primary', 'Button'), ('card-link', 'Link')], label='Style of the link'))])), ('internal_link', wagtail.blocks.StructBlock([('link', wagtail.blocks.PageChooserBlock(label='Link to this site page')), ('text', wagtail.blocks.CharBlock(label='Text of the link', required=True)), ('style', wagtail.blocks.ChoiceBlock(choices=[('', 'Choose style'), ('btn btn-primary', 'Button'), ('card-link', 'Link')], label='Style of the link'))]))], required=False))])))]))], use_json_field=True),
        ),
    ]
