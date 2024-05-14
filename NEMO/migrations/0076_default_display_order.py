# Generated by Django 3.2.25 on 2024-04-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NEMO", "0075_adjustmentrequest_applied"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
        ),
        migrations.AlterField(
            model_name="safetyitemdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
        ),
        migrations.AlterField(
            model_name="staffknowledgebaseitemdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
        ),
        migrations.AlterField(
            model_name="tooldocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
        ),
        migrations.AlterField(
            model_name="userdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
        ),
        migrations.AlterField(
            model_name="userknowledgebaseitemdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
        ),
    ]