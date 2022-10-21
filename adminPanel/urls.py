from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminLogin, name='adminLogin'),
    path('adminHome', views.adminHome, name='adminHome'),
    path('update', views.update, name='update'),
    path('adminLogout', views.adminLogout, name='adminLogout'),
]
