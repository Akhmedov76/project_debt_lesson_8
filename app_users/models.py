from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class UserModel(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    related_name = 'custom_user_permissions',

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
