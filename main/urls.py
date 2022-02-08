from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='main_homepage'),
    path('addPeopleToEvent/', views.addPeopleToEvent),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
]
