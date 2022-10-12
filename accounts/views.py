from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

from .forms import SigninForm

# Create your views here.

def home(request):
  if 'username' in request.session:
    return redirect('workspace')
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
    if 'username' in request.session:
        return redirect('workspace')
  
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SigninForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                request.session['username'] = username
                login(request, user)
                return render(request, 'workspace.html', {'uname':username})
            else:
                messages.error(request, "Wrong username/password")
                return redirect('signin')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SigninForm()

    return render(request, 'signin.html', {'form': form})

def signout(request):
  if 'username' in request.session:
    request.session.flush()
  logout(request)
  messages.success(request, "Logged out successfully.")
  return redirect('home')

def workspace(request):
  if 'username' in request.session:
    return render(request, 'workspace.html')
  return redirect(signin)

def tasks(request):
  if 'username' in request.session:
    return HttpResponse('<h1>Tasks Page</h1>')
  return redirect(signin)
  
def profile(request):
  if 'username' in request.session:
    return HttpResponse('<h1>Student Profile</h1>')
  return redirect(signin)

def contact(request):
  return HttpResponse('<h1>Contact Page</h1>')

