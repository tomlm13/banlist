from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import ListView
from .models import BannedUser
from .forms import BanUserForm
from django.contrib import messages
# Create your views here.
def banuser(request):
    if request.method == 'POST':
        form = BanUserForm(request.POST)
        if form.is_valid():
            form.save()
            banned_username = form.cleaned_data.get('username')
            messages.success(request, "Banned user has been added to the list")
            return redirect('ban_list')
    else:
        form = BanUserForm(request.GET)
    return render(request, 'banuser/ban_user.html', {'form': form})

class BannedUserListView(ListView):
    def get_queryset(self):
        return BannedUser.objects.all()

    template_name='banuser/ban_list.html'
    context_object_name = 'bannedusers'
