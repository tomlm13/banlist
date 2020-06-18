from django.urls import path
from .views import BannedUserListView
from . import views

urlpatterns = [
    path('', BannedUserListView.as_view(), name='ban_list'),
    path('ban_user/', views.banuser, name='ban_user')
]
