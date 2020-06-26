from rest_framework import serializers
from .models import BannedUser

class BannedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannedUser
        fields = ['id','banned_username', 'ban_reason','ban_date']
