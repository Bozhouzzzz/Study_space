# Generated by Django 2.2.28 on 2023-03-16 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_spaces_app', '0014_auto_20230316_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_spaces_app.Post'),
        ),
    ]
