from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User

from .models import Students

from passlib.hash import pbkdf2_sha256
from .forms import LoginForm, CreateStudent, AddStudent

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
                return redirect(adminLogin)
              else:
                messages.error(request, "You are not authorized to access this webpage!!!")
                return redirect('adminLogin')
            else:
                messages.error(request, "Wrong username/password!!!")
                return redirect('adminLogin')

  # if a GET (or any other method) we'll create a blank form
  else:
        form = LoginForm()

  return render(request, 'adminLogin.html', {'form': form})

def adminHome(request):
  if 'username' in request.session:
    students = User.objects.all()
    return render(request, 'adminHome.html', {'students':students})
  return redirect(adminLogin)

def addStudent(request):
  if 'username' in request.session:
    if request.method == 'POST':
      username = request.POST['username']
      fname = request.POST['fname']
      lname = request.POST['lname']
      email = request.POST['email']
      pass1 = request.POST['pass1']
      
      if User.objects.filter(username=username):
        messages.error(request, "User name already exists!!! Please try with differnet username.")
        return redirect(addStudent)
      
      if User.objects.filter(email=email):
        messages.error(request, "Email already registerd!!!")
        return redirect(addStudent)
      
      else:
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, "Added student Succesfully.")
        return redirect(addStudent)
    else:
      form = CreateStudent()
    return render(request, 'addStudent.html', {'form':form})
  return redirect(adminLogin)

def deleteStudent(request, id):
  if 'username' in request.session:
    if request.method == 'POST':
      student = User.objects.get(pk=id)
      student.delete()
      return redirect(adminHome)
  return redirect(adminLogin)

def editStudent(request, id):
  if 'username' in request.session:
    return render(request, 'editStudent.html', {'id':id})
  return redirect(adminLogin)

def adminLogout(request):
  if 'username' in request.session:
    request.session.flush()
  logout(request)
  messages.success(request, "Logged out successfully.")
  return redirect(adminHome)