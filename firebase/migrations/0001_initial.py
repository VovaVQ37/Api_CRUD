# Generated by Django 3.1.8 on 2022-08-17 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcm_django', '0009_alter_fcmdevice_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDevice',
            fields=[
                ('fcmdevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fcm_django.fcmdevice')),
            ],
            options={
                'verbose_name': 'FCM device',
                'abstract': False,
            },
            bases=('fcm_django.fcmdevice',),
        ),
    ]