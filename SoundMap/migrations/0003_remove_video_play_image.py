# Generated by Django 3.0.3 on 2020-05-19 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoundMap', '0002_auto_20200515_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='play_image',
        ),
    ]
