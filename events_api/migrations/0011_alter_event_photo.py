# Generated by Django 4.1.1 on 2022-10-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_api', '0010_alter_event_host_alter_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
