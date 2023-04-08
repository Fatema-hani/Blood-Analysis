from collections import UserList
from django.urls import path
from .views import userlist

urlpatterns = [
    path('users/', userlist.as_view())
]