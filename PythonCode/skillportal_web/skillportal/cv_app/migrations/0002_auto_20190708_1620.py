# Generated by Django 2.0.7 on 2019-07-08 10:35

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('password', models.CharField(max_length=32)),
                ('confirm_password', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]