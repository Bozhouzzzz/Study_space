# Generated by Django 2.2.28 on 2023-03-11 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_spaces_app', '0003_auto_20230311_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
