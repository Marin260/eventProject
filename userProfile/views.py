from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, UpdateView
from .models import *
from main.models import Event
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


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
        context['event_count'] = allEvents.count()
        return context


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['bio', 'image', 'location', 'webstranica', 'firma']

    def get_object(self):
        """
        Get username in url instead of id
        """
        
        UserName= self.kwargs.get("username")
        
        tmp = get_object_or_404(User, username=UserName)

        return get_object_or_404(Profile, user=tmp)

    def form_valid(self, form):
        #am I editing my own profile?
        form.instance.user = self.request.user
        print(form.instance.image)
        return super().form_valid(form)

    def test_func(self):
        """
        UserPassesTestMixin will run this function to test if
        current loged in user is the event author
        403 Forbidden if he is not the author
        """
        profil = self.get_object()
        if self.request.user == profil.user:  #uzimas objekt sesija i usporedujes sa objektom profila
            return True
        return False

def profileCreation(request):
    if Profile.objects.filter(user=request.user).exists():
        print ("This user already has a profile")
    else:
        noviProfil = Profile(user=request.user)
        noviProfil.save()
    #return redirect("main_homepage")
    return redirect("profile-detail", username = request.user.username)

