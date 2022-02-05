from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('signUp/', views.signUp),
    path('login/', views.login),

]
