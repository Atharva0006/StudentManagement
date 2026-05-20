from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Connect app URLs
    path('', include('studentapp.urls')),
]