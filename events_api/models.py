from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import CustomUser

def file_size(value):  # add this to some file where you can import it from TODO not working now
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    photo = models.ImageField(blank=True, null=True, validators=[file_size])
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    city = models.CharField(max_length=120)
    approved = models.BooleanField(default=False)
    participants = models.ManyToManyField(CustomUser, related_name="eventparticipants", blank=True)
    favourites = models.ManyToManyField(CustomUser, related_name="eventfavourites", blank=True)
    host = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="eventhost")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["event_start"]

    def count_participants(self):
        return self.participants.count()
