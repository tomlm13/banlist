from django import forms
from django.forms import ModelForm
from .models import BannedUser

class BanUserForm(ModelForm):
    banned_username=forms.CharField()
    ban_reason=forms.CharField()
    class Meta:
        model = BannedUser
        fields = ['banned_username', 'ban_reason']
        widgets = {'ban_date': forms.HiddenInput()}
