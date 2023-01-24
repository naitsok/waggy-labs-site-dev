# Generated by Django 4.1.3 on 2023-01-24 12:11

from django.db import migrations
import waggylabs.blocks.icon
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('waggylabs', '0012_sidebar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitepage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StructBlock([('tabs_style', wagtail.blocks.ChoiceBlock(choices=[('', 'Choose tabs style'), ('nav nav-tabs', 'Tabs'), ('nav nav-pills', 'Pills'), ('nav nav-pills nav-fill', 'Wide pills')], label='Tabs style')), ('buttons_style', wagtail.blocks.ChoiceBlock(choices=[('', 'Choose button style'), ('btn btn-primary', 'Button primary'), ('btn btn-secondary', 'Button secondary'), ('btn btn-success', 'Button success'), ('btn btn-danger', 'Button danger'), ('btn btn-warning', 'Button warning'), ('btn btn-info', 'Button info'), ('btn btn-outline-primary', 'Button outline primary'), ('btn btn-outline-secondary', 'Button outline secondary'), ('btn btn-outline-success', 'Button outline success'), ('btn btn-outline-danger', 'Button outline danger'), ('btn btn-outline-warning', 'Button outline warning'), ('btn btn-outline-info', 'Button outline info'), ('link-default', 'Default link'), ('link-primary', 'Primary link'), ('link-secondary', 'Secondary link'), ('link-success', 'Success link'), ('link-danger', 'Danger link'), ('link-warning', 'Warning link'), ('link-info', 'Info link'), ('link-light', 'Light link'), ('link-dark', 'Dark link')], label='Tab buttons style')), ('tabs_font_size', wagtail.blocks.ChoiceBlock(choices=[('', 'Choose font size'), ('fs-6', 'Normal'), ('fs-5', 'Bigger'), ('fs-4', 'Big'), ('fs-3', 'Larger'), ('fs-2', 'Large')], label='Tabs font size')), ('tabs_orientation', wagtail.blocks.ChoiceBlock(choices=[('', 'Choose button orientation'), ('horizontal', 'Horizontal'), ('vertical', 'Vertical')], label='Tabs orientation')), ('tabs_justify', wagtail.blocks.ChoiceBlock(choices=[('', 'Choose horizontal alignment'), ('justify-content-start', 'Align left'), ('justify-content-center', 'Align center'), ('justify-content-end', 'Align right')], label='Tabs orientation')), ('items', wagtail.blocks.StreamBlock([('table_of_contents', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title to appear on the tab.', label='Title', required=False)), ('icon', waggylabs.blocks.icon.IconBlock(label='Icon', required=False))])), ('visuals', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title to appear on the tab.', label='Title', required=False)), ('icon', waggylabs.blocks.icon.IconBlock(label='Icon', required=False)), ('include_embeds', wagtail.blocks.BooleanBlock(label='Include embeds', required=False)), ('include_equations', wagtail.blocks.BooleanBlock(label='Include equations', required=False)), ('include_figures', wagtail.blocks.BooleanBlock(label='Include figures', required=False)), ('include_listings', wagtail.blocks.BooleanBlock(label='Include listings', required=False)), ('include_tables', wagtail.blocks.BooleanBlock(label='Include tables', required=False))])), ('citations', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title to appear on the tab.', label='Title', required=False)), ('icon', waggylabs.blocks.icon.IconBlock(label='Icon', required=False))]))]))]))], blank=True, use_json_field=True),
        ),
    ]
