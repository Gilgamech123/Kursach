from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)

# Create your models here.

class Customer(models.Model):
    passport_data = models.CharField(max_length=150)
    snills = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Employeer(models.Model):
    position = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
