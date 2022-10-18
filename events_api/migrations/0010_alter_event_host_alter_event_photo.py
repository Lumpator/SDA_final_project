# Generated by Django 4.1.1 on 2022-10-18 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import events_api.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events_api', '0009_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='eventhost', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[events_api.models.file_size]),
        ),
    ]
