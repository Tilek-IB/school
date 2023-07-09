# Generated by Django 4.2.2 on 2023-07-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0003_alter_teacher_date_of_birth_alter_teacher_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('teacher', models.ManyToManyField(related_name='sciences', to='teachers.teacher')),
            ],
        ),
    ]
