# Generated by Django 5.0.1 on 2024-04-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hiken", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="templatehtml",
            name="placeholder",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name="templatehtml",
            name="template",
            field=models.TextField(
                help_text="Put the placeholder around double curly bracket in template as template_tags."
            ),
        ),
    ]
