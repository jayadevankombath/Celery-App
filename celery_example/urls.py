from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('notify/', include('notifications.urls')),
    path('admin/', admin.site.urls),
    
]
