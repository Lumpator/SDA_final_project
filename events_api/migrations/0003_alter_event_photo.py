# Generated by Django 4.1.1 on 2022-09-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_api', '0002_alter_event_participants_alter_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, upload_to='events_api/media/event_photos'),
        ),
    ]
