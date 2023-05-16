# Generated by Django 4.1.9 on 2023-05-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("waggylabs", "0048_site_settings"),
    ]

    operations = [
        migrations.AddField(
            model_name="waggylabssettings",
            name="navbar_hover_link_color",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Specifies the color and opacity for the navigation bar links during hover. If none specified, the default theme color is used.",
                max_length=25,
                verbose_name="Navigation bar hover link color",
            ),
        ),
    ]
