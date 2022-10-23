from dataclasses import fields
from django import forms
from .models import Students
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Username'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Enter Your Password'}), label="Password")

class CreateStudent(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Username'}), max_length=100)
    fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your First Name'}), max_length=100, label="First Name")
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Last Name'}), max_length=100, label="Last Name")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Email Address'}), max_length=100)
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Create a Password'}), label="Password")

class EditStudent(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            # 'password': 'Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'}),
            'first_name': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'}),
            'last_name': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'}),
            'email': forms.EmailInput(attrs={'class':'form-control mt-2 mb-2'}),
            # 'password': forms.PasswordInput(attrs={'class':'form-control mt-2 mb-2'}),
        }
        help_texts = {
            'username': None,
            'email': None,
        }