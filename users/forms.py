from dataclasses import field
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()   #only extra fields to be included are to be named

    class Meta:
        model = User
        fields = ['username','email','password1','password2']  #this is the same order in which fields are displayed in registration form



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()   #only extra fields to be included are to be named

    class Meta:
        model = User
        fields = ['username','email']  #this is the same order in which fields are displayed in registration form


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']