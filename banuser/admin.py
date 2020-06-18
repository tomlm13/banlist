from django.contrib import admin

# Register your models here.
from .models import BannedUser

admin.site.register(BannedUser)
