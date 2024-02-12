from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import CustomerUserManager

# In this we are customezing Abstract User
# which is Built in User
class CustomUser(AbstractUser):
    # we set username None because we want to use email 
    # as unique key in django instead of username
    username=None
    # define email and set null False
    email = models.EmailField(unique=True,null=False)
    # it says use email as username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # CustomerUserManager we use because we can't use bulit in UserManager now 
    # as we are using email as unique key in django
    objects =CustomerUserManager()
    def __str__(self):
            return self.email
