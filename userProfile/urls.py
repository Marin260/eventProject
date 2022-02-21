from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.ProfileDetailView.as_view(), name='profile-detail'),
]
