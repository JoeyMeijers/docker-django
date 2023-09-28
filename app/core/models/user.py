"""
Database models
"""
from django.db import models
from core.models.user_manager import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Assign user manager
    objects = UserManager()

    USERNAME_FIELD = 'email'
