from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib import auth
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


###########################
# from django.conf import settings
# from django.db.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token


# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance)


###########################

class Manager(User, auth.models.PermissionsMixin):
    """
    email,password,first_name,last_name fields are inherited
    form User inbuild Model,  DRY:)
    """
    company = models.CharField(max_length=50,null = True,blank = True)
    address = models.TextField(blank=True)
    dob = models.DateField(null=True)
    def __str__(self):
        return self.username
    

class Employee(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=254)
    mobile_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$',message="Phone number must be entered in the formet: '+999999999999'.up to 15 digits allowed.")
    mobile = models.CharField(
        validators=[mobile_regex], max_length=17, blank=True, unique = True)
    dob = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("manager_app:employee_list")
    

    def __str__(self):
        return self.email


    


