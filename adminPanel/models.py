from django.db import models

# Create your models here.

class Student(models.Model):
  username = models.CharField(max_length=50)
  fname = models.CharField(max_length=70)
  lname = models.CharField(max_length=70)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=200)
  
  
