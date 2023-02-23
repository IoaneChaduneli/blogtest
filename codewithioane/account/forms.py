from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='required. Add valid email adress')

    class Meta:
        model = Account
        fields = ['email', 'username', 'password1', 'password2']
       

