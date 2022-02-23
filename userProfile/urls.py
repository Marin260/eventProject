from django.urls import path
from . import views

urlpatterns = [
    path('profileCreate/', views.profileCreation),
    path('<str:username>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('<str:username>/edit', views.ProfileUpdateView.as_view(), name='profile-edit')
]
