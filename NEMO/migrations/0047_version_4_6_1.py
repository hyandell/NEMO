# Generated by Django 3.2.20 on 2023-07-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0046_version_4_6_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customization',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
