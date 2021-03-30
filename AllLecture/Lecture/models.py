from django.db import models
from django.contrib.auth.models import User

class UserInfoModel(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200,unique=True)

class UserLoginModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username

