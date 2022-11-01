from dataclasses import fields
import email
from logging import PlaceHolder
from tkinter import Widget
from unicodedata import name
from django import forms
from .models import Customer,Booked
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomerForm(UserCreationForm):
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password from numbers,letters and special characters '}))
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput({'placeholder': 'Username...'}),
            'email': forms.TextInput({'placeholder': 'email@domain.com'}),
        }
        fields = ['username','email','password1','password2']

class BookedForm(forms.ModelForm):
    class Meta:
        model = Booked
        fields = ['name', 'email', 'number']