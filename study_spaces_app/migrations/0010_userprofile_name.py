# Generated by Django 2.2.28 on 2023-03-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_spaces_app', '0009_auto_20230316_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]