# Generated by Django 3.1.8 on 2022-08-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220614_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]