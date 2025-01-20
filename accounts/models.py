from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            username=username,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, username, password, **extra_fields):
        extra_fields["is_active"] = True
        extra_fields["is_superuser"] = True
        return self._create_user(
            username=username,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=_("username"), unique=True, max_length=10)
    is_superuser = models.BooleanField(verbose_name=_("is_superuer"), default=False)
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
