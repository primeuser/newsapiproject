from django import forms
from .models import *
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description','date_created',
                  'image', 'author', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the in