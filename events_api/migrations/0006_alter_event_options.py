# Generated by Django 4.1.1 on 2022-10-06 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_api', '0005_remove_event_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_start']},
        ),
    ]
