from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class UserPermissions(models.Model):
    level = models.CharField(max_length=60)

    def __str__(self):
        return self.level


class CustomUser(AbstractUser):
    permission = models.ForeignKey(UserPermissions, on_delete=models.SET_NULL, null=True, default=1)

