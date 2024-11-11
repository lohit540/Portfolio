from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mywebpage.urls')),  # Point root URL to "mywebpage"
]
