# Generated by Django 3.1.7 on 2021-03-29 10:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questboard', '0002_quest'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='questboard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questboard.questboard'),
            preserve_default=False,
        ),
    ]
