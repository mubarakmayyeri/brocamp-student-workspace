from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.tasks, name='tasks'),
    path('profile', views.profile, name='profile'),
    path('contact', views.contact, name='contact')
]
