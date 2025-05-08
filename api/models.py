from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAccount(AbstractUser):
    staff_category = models.CharField(max_length=100)

