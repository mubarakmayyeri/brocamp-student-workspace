from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
  return render(request, 'home.html')

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    fname = request.POST['fname']
    lname = request.POST['lname']
    emailpass1 = request.POST['emailpass1']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
  
  return render(request, 'signup.html')

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    pass1 = request.POST['pass1']
    
    user = authenticate(username=username, password=pass1)
    
    if user is not None:
      login(request, user)
      return render(request, 'index.html', {'uname':username})
      
    else:
      messages.error(request, "Wrong username/password")
      return redirect('signin')
    
    
  return render(request, 'signin.html')
