from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return render(request, 'index.html')

def tasks(request):
  return HttpResponse('<h1>Tasks Page</h1>')

def profile(request):
  return HttpResponse('<h1>Student Profile</h1>')

def contact(request):
  return HttpResponse('<h1>Contact Page</h1>')