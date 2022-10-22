from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminLogin, name='adminLogin'),
    path('adminHome', views.adminHome, name='adminHome'),
    path('editStudent', views.editStudent, name='editStudent'),
    path('deleteStudent/<int:id>', views.deleteStudent, name='deleteStudent'),
    path('adminLogout', views.adminLogout, name='adminLogout'),
]
