from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Form for new user registration (extends Django's built-in UserCreationForm)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Adds an email field to the default form
    
    class Meta:
        model = User  # Links form to User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields shown in the registration form
        

# Form for updating username and email of an existing user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']


# Form for updating profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
