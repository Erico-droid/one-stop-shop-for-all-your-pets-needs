from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db import DefaultConnectionProxy, models      #awein matlab

# Create your models here.

class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_serviceprovider = models.BooleanField(default=False)
    is_rescue_service = models.BooleanField(default=False)
    is_vet = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    # user_description = models.TextField(default = "Some Rich Text")

class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.CharField(max_length = 120)
    address2 = models.CharField(max_length = 120, null = True, blank = True)
    city = models.CharField(max_length = 120, null = True, blank = True)
    state = models.CharField(max_length = 120, null = True, blank = True)
    country = models.CharField(max_length = 120, null = True, blank = True)
    zipcode = models.CharField(max_length = 25)
    phone_number = models.CharField(max_length = 25)
    shipping = models.BooleanField(default = True)
    billing = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
         verbose_name = "User Address"
         verbose_name_plural = "User Adresses"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)   #This establishes a 1-1 relationship between objects of 2 classes ie here it means 1 user can only have 1 profile and vice versa
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # Add more fields here later. Don't forget to run migrations
    def __str__(self):
        return f'{self.user.username} Profile'

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    product_category = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username         #fix if problem

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_approved = models.BooleanField(default=False)
    service_information = models.TextField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username


class RescueServices(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_approved = models.BooleanField(default=False)
    service_information = models.TextField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    class Meta:
         verbose_name = "Rescue Service"
         verbose_name_plural = "Rescue servies"

class Vet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_approved = models.BooleanField(default=False)
    experience = models.TextField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username
