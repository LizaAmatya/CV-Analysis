# Generated by Django 2.0.7 on 2019-07-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0003_remove_candidate_confirm_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='last_name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='user',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='password',
            new_name='password1',
        ),
    ]