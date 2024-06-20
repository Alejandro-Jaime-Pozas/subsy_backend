"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)  # this supports adding multiple dbs if needed (best practice)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        superuser = self.create_user(email, password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True, blank=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # This assigns UserManager to manage the User model, providing methods to create users and superusers.

    USERNAME_FIELD = 'email'  # This sets the field used for authentication to be the email address instead of the default username.


class Company(models.Model):
    # TODO create the name field based on the domain name from the user's email IF user checks the option for 'company you're using for subsy is the same as your email domain?'; should maybe make the name unique, since there should really only be unique companies...based on unique domains...
    """Company in the system."""
    name = models.CharField(max_length=255, blank=False)  # in theory this should not allow blank strings as input, therefore no null values will exist in db
    domain = models.CharField(max_length=255, blank=False, unique=True)


class LinkedBank(models.Model):
    """Linked Bank (plaid item) in the system."""
    name = models.CharField(max_length=255)
    web_portal_url = models.URLField(max_length=5000)  # maybe a better way to acct for long urls?


class BankAccount(models.Model):
    """Bank account in the system."""
    name = models.CharField(max_length=255, blank=False)
    
