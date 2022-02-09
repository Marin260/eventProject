from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='main_homepage'),
    path('addPeopleToEvent/', views.addPeopleToEvent),
    path('event/<int:pk>/<slug:slug>', views.EventDetailView.as_view(), name='event-detail'),
    path('event/new/', views.EventCreateView.as_view(), name='create-event')
]
