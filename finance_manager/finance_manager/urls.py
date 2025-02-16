from django.contrib import admin
from django.urls import path, include
from . import views  # Import the views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
]
