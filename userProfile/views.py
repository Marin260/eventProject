from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import *


class ProfileDetailView(DetailView):
    model = Profile

    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(User, username=UserName)
