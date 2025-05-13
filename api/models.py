from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self , employee_id , password=None , **extra_fields):
        if not employee_id:
            raise ValueError("The Employee ID must be set.")
        
        user = self.model(employee_id=employee_id , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self , employee_id, password=None , **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        user = self.create_user(employee_id, password, **extra_fields)

        return user
    

class UserAccount(AbstractUser , PermissionsMixin):
    employee_id = models.CharField(max_length=8, unique=True)
    email = models.EmailField(blank=True)
    staff_category = models.CharField(max_length=100)

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.employee_id
    
