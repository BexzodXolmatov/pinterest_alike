import pathlib
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from account.managers import UserManager


def avatar_upload_handler(_, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f"pinterest/avatar/{new_fname}/original{fpath.suffix}"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    profile_image = models.ImageField(upload_to=avatar_upload_handler)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
