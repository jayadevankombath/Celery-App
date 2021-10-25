from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.update_status, name='update_status'),
    
]