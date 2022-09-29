from django.db import models

from accounts.models import CustomUser


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    photo = models.FilePathField(path="events_restapi/media/event_photos", null=True)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    city = models.CharField(max_length=120)
    approved = models.BooleanField(default=False)
    participants = models.ManyToManyField(CustomUser, related_name="eventparticipants")
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="eventhost")