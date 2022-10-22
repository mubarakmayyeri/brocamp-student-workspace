from dataclasses import fields
from django import forms
from .models import Students

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Username'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Enter Your Password'}), label="Password")

class CreateStudent(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Username'}), max_length=100)
    fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your First Name'}), max_length=100, label="First Name")
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Last Name'}), max_length=100, label="Last Name")
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Email Address'}), max_length=100)
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Create a Password'}), label="Password")

class AddStudent(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['username', 'fname', 'lname', 'email', 'password']
        labels = {
            'username': 'Username',
            'fname': 'First Name',
            'lname': 'Last Name',
            'email': 'Email Address',
            'password': 'Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'}),
            'fname': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'}),
            'lname': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'}),
            'email': forms.EmailInput(attrs={'class':'form-control mt-2 mb-2'}),
            'password': forms.PasswordInput(attrs={'class':'form-control mt-2 mb-2'}),
        }