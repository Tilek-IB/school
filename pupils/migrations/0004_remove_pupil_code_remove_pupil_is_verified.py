# Generated by Django 4.2.2 on 2023-07-08 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0003_remove_pupil_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupil',
            name='code',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='is_verified',
        ),
    ]
