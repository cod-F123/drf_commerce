from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Email Field is required !")

        email = self.normalize_email(email)

        user = self.model(email = email,**extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff Field must be True !.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser Field must be True !.")
        
        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return self.email

