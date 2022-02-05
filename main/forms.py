from django.forms import ModelForm, fields
from .models import AdminKorisnici
from django import forms

class AdminSingUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AdminKorisnici
        fields = '__all__'

class AdminLogInForm(ModelForm):
    class Meta:
        model = AdminKorisnici
        fields = '__all__'
