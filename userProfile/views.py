from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import *
from main.models import Event


class ProfileDetailView(DetailView):
    model = Profile

    def get_object(self):
        """
        Get username in url instead of id
        """
        UserName= self.kwargs.get("username")
        return get_object_or_404(User, username=UserName)

    def get_context_data(self, **kwargs):
        """
        Get extra context for display in detail view
        extra context: all the events created by the user detailed user
        """
        context = super().get_context_data(**kwargs)
        allEvents = Event.objects.filter(autor_objave__username=self.get_object())
        context['event_list'] = allEvents
        return context
