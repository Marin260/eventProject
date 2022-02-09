from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hiddenadmin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('', include('main.urls'))
]
