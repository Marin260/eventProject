from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('NoAdminSite/', admin.site.urls),
    path('', include('allauth.urls')),
    path('', include('main.urls')),
    path('', include('userProfile.urls')),
]

handler404 = 'main.views.handler404' #needed for custom 404
handler403 = 'main.views.handler403' #needed for custom 403
