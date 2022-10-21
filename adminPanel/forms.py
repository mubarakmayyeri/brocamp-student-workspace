from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Username'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Enter Your Password'}), label="Password")
    