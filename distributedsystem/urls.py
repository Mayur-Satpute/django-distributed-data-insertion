from django.contrib import admin
from django.urls import path
from treadapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("run/",run_all),

]
