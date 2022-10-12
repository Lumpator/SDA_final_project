from django.db import models

from accounts.models import CustomUser


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    photo = models.ImageField(upload_to="events_api/media/event_photos", blank=True, null=True)
    # photo = "https://picsum.photos/1280/720"
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    city = models.CharField(max_length=120)
    approved = models.BooleanField(default=False)
    participants = models.ManyToManyField(CustomUser, related_name="eventparticipants", blank=True)
    favourites = models.ManyToManyField(CustomUser, related_name="eventfavourites", blank=True)
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="eventhost")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["event_start"]