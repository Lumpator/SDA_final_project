from django.db import models

from accounts.models import CustomUser
from events_api.models import Event


# Create your models here.
class Message(models.Model):
    body = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="usermsg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created", "-updated"]

    def __str__(self):
        return self.body