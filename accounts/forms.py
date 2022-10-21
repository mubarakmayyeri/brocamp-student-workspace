from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Your Username'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}), label="Password")
    
class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Username'}), max_length=100)
    fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your First Name'}), max_length=100, label="First Name")
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Last Name'}), max_length=100, label="Last Name")
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter Your Email Address'}), max_length=100)
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Create a Password'}), label="Password")
    pass2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Confirm Your Password'}), label="Confirm Password")