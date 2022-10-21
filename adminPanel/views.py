from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import LoginForm

# Create your views here.

def adminLogin(request):
  if 'username' in request.session:
        return redirect('adminHome')

    # if this is a POST request we need to process the form data
  if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            
            if user is not None:
              if user.is_superuser:
                request.session['username'] = username
                login(request, user)
                return render(request, 'adminHome.html')
              else:
                messages.error(request, "You are not authorized to access this webpage!!!")
                return redirect('adminLogin')
            else:
                messages.error(request, "Wrong username/password!!!")
                return redirect('adminLogin')

  # if a GET (or any other method) we'll create a blank form
  else:
        form = LoginForm()

  return render(request, 'login.html', {'form': form})

def adminHome(request):
  if 'username' in request.session:
    return render(request, 'adminHome.html')
  return redirect(adminLogin)

def update(request):
  if 'username' in request.session:
    return render(request, 'update.html')
  return redirect(adminLogin)

def adminLogout(request):
  if 'username' in request.session:
    request.session.flush()
  logout(request)
  messages.success(request, "Logged out successfully.")
  return redirect(adminHome)