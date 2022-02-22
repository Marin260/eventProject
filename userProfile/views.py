from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, UpdateView
from .models import *
from main.models import Event
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class ProfileDetailView(UserPassesTestMixin, DetailView):
    model = Profile

    def test_func(self):
        UserName= self.kwargs.get("username")
        tmp = get_object_or_404(User, username=UserName)
        post = self.get_object()
        if self.request.user == tmp:
            if Profile.objects.filter(user=tmp).exists():
                print ("Ovaj user ima profil")
            else:
                print ("Ovaj user nema profil")
                noviProfil = Profile(user=tmp)
                noviProfil.save()
            return True
        return True
    
    def get_object(self):
        """
        Get username in url instead of id
        """
        
        UserName= self.kwargs.get("username")
        


        #if Profile.objects.filter(id=get_object_or_404(User, id=tmp).id).exists():
        #    print("It exists")
        #else:
        #    print("Ne postoji")
        
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
        print (profil)
        if self.request.user == profil.user:  #uzimas objekt sesija i usporedujes sa objektom profila
            return True
        return False
