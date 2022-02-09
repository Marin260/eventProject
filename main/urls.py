from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='main_homepage'),
    path('addPeopleToEvent/', views.addPeopleToEvent),
    path('event/<int:pk>/<slug:slug>', views.EventDetailView.as_view(), name='event-detail'),

    path('event/new/', views.EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/<slug:slug>/update', views.EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/<slug:slug>/delete', views.EventDeleteView.as_view(), name='event-delete')
]
