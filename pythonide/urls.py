from django.contrib import admin
from django.urls import path
from app.views import pythonide

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pythonide/', pythonide),
]
