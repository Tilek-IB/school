# Generated by Django 4.2.2 on 2023-07-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='science',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название предмета'),
        ),
    ]
