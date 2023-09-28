"""
User manager class
"""
from django.contrib.auth.models import BaseUserManager
from typing import Optional


class UserManager(BaseUserManager):
    """User manager class"""

    def create_user(self, email: str, password: Optional[str] = None,
                    **kwargs):
        """Create, save and return user"""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: Optional[str]):
        """Create and return superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
