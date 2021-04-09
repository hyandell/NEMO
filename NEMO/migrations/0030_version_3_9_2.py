# Generated by Django 2.2.20 on 2021-04-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0028_version_3_9_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='badge_number',
            field=models.CharField(blank=True, help_text='The badge number associated with this user. This number must correctly correspond to a user in order for the tablet-login system (in the lobby) to work properly.', max_length=50, null=True, unique=True),
        ),
    ]
