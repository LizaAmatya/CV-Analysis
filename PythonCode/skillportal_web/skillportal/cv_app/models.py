from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.forms import ModelForm
from django.db import connection

# Create your models here.
class Candidate(models.Model):
    username = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = PhoneField()
    password1 = models.CharField(max_length=32)
    # password2 = models.CharField(max_length=32)



    def __str__(self):
        return self.username