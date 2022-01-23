# Generated by Django 2.2.24 on 2021-10-26 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0035_version_3_14_0'),
    ]

    def rename_customization(apps, schema_editor):
        Customization = apps.get_model("NEMO", "Customization")
        try:
            buddy_board_desc_old = Customization.objects.get(name="buddy_board_disclaimer")
            Customization.objects.create(name="buddy_board_description", value=buddy_board_desc_old.value)
            buddy_board_desc_old.delete()
        except:
            pass

    operations = [
        migrations.RunPython(rename_customization),
        migrations.AlterField(
            model_name='landingpagechoice',
            name='notifications',
            field=models.CharField(blank=True, choices=[('news', 'News creation and updates - notifies all users'), ('safetyissue', 'New safety issues - notifies staff only'), ('buddyrequest', 'New buddy request - notifies all users'), ('buddyrequestmessage', 'New buddy request reply - notifies request creator and users who have replied'), ('temporaryphysicalaccessrequest', 'New access request - notifies other users on request and reviewers')], help_text="Displays a the number of new notifications for the user. For example, if the user has two unread news notifications then the number '2' would appear for the news icon on the landing page.", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='category',
            field=models.IntegerField(choices=[(0, 'General'), (1, 'System'), (2, 'Direct Contact'), (3, 'Broadcast Email'), (4, 'Timed Services'), (5, 'Feedback'), (6, 'Abuse'), (7, 'Safety'), (8, 'Tasks'), (9, 'Access Requests')], default=0),
        ),
        migrations.AlterField(
            model_name='physicalaccesslevel',
            name='schedule',
            field=models.IntegerField(choices=[(0, 'Anytime'), (1, 'Weekdays'), (2, 'Weekends')]),
        ),
        migrations.AddField(
            model_name='physicalaccesslevel',
            name='allow_user_request',
            field=models.BooleanField(default=False, help_text='Check this box to allow users to request this access temporarily in "Access requests"'),
        ),
        migrations.CreateModel(
            name='TemporaryPhysicalAccessRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='The date and time when the request was created.')),
                ('last_updated', models.DateTimeField(auto_now=True, help_text='The last time this request was modified.')),
                ('description', models.TextField(blank=True, help_text='The description of the request.', null=True)),
                ('start_time', models.DateTimeField(help_text='The requested time for the access to start.')),
                ('end_time', models.DateTimeField(help_text='The requested time for the access to end.')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Denied'), (3, 'Expired')], default=0)),
                ('deleted', models.BooleanField(default=False, help_text="Indicates the request has been deleted and won't be shown anymore.")),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_requests_created', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(blank=True, help_text='The last user who modified this request.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='access_requests_updated', to=settings.AUTH_USER_MODEL)),
                ('other_users', models.ManyToManyField(blank=True, help_text='Select the other users requesting access.', to=settings.AUTH_USER_MODEL)),
                ('physical_access_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NEMO.PhysicalAccessLevel')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='access_requests_reviewed', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_time'],
            },
        ),
    ]
