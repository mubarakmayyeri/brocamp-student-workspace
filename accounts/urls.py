from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('workspace', views.workspace, name='workspace'),
    path('tasks', views.tasks, name='tasks'),
    path('profile', views.profile, name='profile'),
    path('contact', views.contact, name='contact')
]
