from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.emptyRedirect, name='landing'),
    path('browse/', views.homepage, name='main_homepage'),
    path('addPeopleToEvent/', views.addPeopleToEvent),
    path('event/<int:pk>/<slug:slug>/', views.EventDetailView.as_view(), name='event-detail'),
    path('landingtest/', views.landing, name="landingtest"),

    path('event/new/', views.EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/<slug:slug>/update/', views.EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/<slug:slug>/delete/', views.EventDeleteView.as_view(), name='event-delete'),

    #path('<str:username>/', views.AuthorProfileDetailView.as_view(), name='autor-detail'),
]

if settings.DEBUG: #only in DEBUG mode, change this b4 deployment
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.handler404' #needed for custom 404
handler403 = 'main.views.handler403' #needed for custom 403