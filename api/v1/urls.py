from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.users.urls')),
]
