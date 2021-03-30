from django import forms
from django.contrib.auth.models import User
from .models import UserLoginModel

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserPortfolioForm(forms.ModelForm):
    class Meta():
        model = UserLoginModel
        fields = ('portfolio_site','profile_pic')