# Generated by Django 2.2.3 on 2019-07-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='job_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]