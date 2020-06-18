from django.db import models
from datetime import datetime

# Create your models here.
class BannedUser(models.Model):
    banned_username = models.CharField(max_length=50)
    ban_date = models.DateTimeField(auto_now_add=True, blank=True)
    ban_reason = models.CharField(max_length=200)

    def __str__(self):
        return self.banned_username
