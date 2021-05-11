from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('otp/', otp),
    path('verify/', verify),
    path('dash/', dash),
    path('pythonide/', pythonide),
    path('create/', create),
    path('logout/', logout),
    path('checklogin/', checklogin),
]
