from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager


# User class code here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True, )
    nickname = models.CharField(max_length=20, unique=True, )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    points = models.IntegerField(default=0)
    profile = models.CharField(
        max_length=10,
        choices=(
            ("reader", "reader"),
            ("basic", "basic"),
            ("advanced", "advanced"),
            ("moderator", "moderator"),
        ),
        default="reader"
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    class Meta:
        db_table = "auth_api_user"
