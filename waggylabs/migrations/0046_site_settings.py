# Generated by Django 4.1.9 on 2023-05-15 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("waggylabs", "0045_site_settings"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="waggylabssettings", name="results_per_page",
        ),
        migrations.AddField(
            model_name="waggylabssettings",
            name="search_results_per_page",
            field=models.IntegerField(
                default=10,
                validators=[
                    django.core.validators.MinValueValidator(
                        1,
                        message="Number of search results per page cannot be less than 1.",
                    )
                ],
                verbose_name="Number of search results per page",
            ),
        ),
        migrations.AlterField(
            model_name="waggylabssettings",
            name="first_page_icon",
            field=models.CharField(
                blank=True,
                help_text="Icon for the first button text.",
                max_length=255,
                verbose_name="First page button icon",
            ),
        ),
        migrations.AlterField(
            model_name="waggylabssettings",
            name="first_page_text",
            field=models.CharField(
                blank=True,
                help_text="Text for the first button text.",
                max_length=255,
                verbose_name="First page button text",
            ),
        ),
        migrations.AlterField(
            model_name="waggylabssettings",
            name="last_page_icon",
            field=models.CharField(
                blank=True,
                help_text="Icon for the last button text.",
                max_length=255,
                verbose_name="Last page button icon",
            ),
        ),
        migrations.AlterField(
            model_name="waggylabssettings",
            name="last_page_text",
            field=models.CharField(
                blank=True,
                help_text="Text for the last button text.",
                max_length=255,
                verbose_name="Last page button text",
            ),
        ),
        migrations.AlterField(
            model_name="waggylabssettings",
            name="next_page_icon",
            field=models.CharField(
                blank=True,
                help_text="Icon for the next button text.",
                max_length=255,
                verbose_name="Next page button icon",
            ),
        ),
        migrations.AlterField(
            model_name="waggylabssettings",
            name="next_page_text",
            field=models.CharField(
                blank=True,
                help_text="Text for the next button text.",
                max_length=255,
                verbose_name="Next page button text",
            ),
        ),
        migrations.AlterField(
            model_name="waggylabssettings",
            name="previous_page_icon",
            field=models.CharField(
                blank=True,
                help_text="Icon for the previous button text.",
                max_length=255,
                verbose_name="Previous page button icon",
            ),
        ),
        migrations.AlterField(
            model_name="waggylabssettings",
            name="previous_page_text",
            field=models.CharField(
                blank=True,
                help_text="Text for the previous button text.",
                max_length=255,
                verbose_name="Previous page button text",
            ),
        ),
    ]
