from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resident(models.Model) :
    name = models.CharField(max_length = 10000)
    phone = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 254)
    building = models.CharField(max_length = 10000)
    date_of_birth = models.DateField(auto_now = False, auto_now_add = False)
    rent = models.DecimalField(max_digits = 10, decimal_places = 2)
    token = models.DecimalField(max_digits = 10, decimal_places = 2)
    contract_start_date = models.DateField(auto_now = False, auto_now_add = False)
    contract_end_date = models.DateField(auto_now = False, auto_now_add = False)
    move_in_date = models.DateField(auto_now = False, auto_now_add = False)
    move_out_date = models.DateField(auto_now = False, auto_now_add = False)

    def __str__(self):
        return self.name

class Employee(models.Model) :
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = None)
    phone = models.CharField(max_length = 20)

    def __str__(self):
        return self.user.first_name

class Event(models.Model) :
    name = models.CharField(max_length = 10000)
    date = models.DateField(auto_now = False, auto_now_add = False)
    description = models.TextField()

    def __str__(self):
        return self.name