from django.db import models
from django.contrib.auth import models as auth_models

from petstagram.accounts.managers import PetstagramUserManager

"""
1. create model extending.....
2. configure this model in settings.py
3. create user manager
"""
# Create your models here.


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()
