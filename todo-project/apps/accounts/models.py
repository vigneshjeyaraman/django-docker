from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)

class UserManager(BaseUserManager):
    """Custom user manager to create users and superuser"""
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User mush have an valid email.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """Create Superuser"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""

    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)    

    objects = UserManager()

    USERNAME_FIELD = 'email'

