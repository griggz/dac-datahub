from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from accounts.utils import unique_slug_generator_auth

import dataHub.settings as settings


class CustomUserManager(BaseUserManager):

    def create_user(self, email, nickname, password):
        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, nickname=None):
        user = self.create_user(email=email, nickname=nickname, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.save()
        return user


class Apps(models.Model):
    app_name = models.CharField(max_length=5000, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.app_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class User(PermissionsMixin, AbstractBaseUser):
    first_name = models.CharField(max_length=5000, blank=True, null=True)
    last_name = models.CharField(max_length=5000, blank=True, null=True)
    email = models.EmailField(max_length=5000, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    meta = models.TextField(default='{}')
    slug = models.SlugField(unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


# PRE SAVE
def user_pre_save_activation_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_auth(instance)

pre_save.connect(user_pre_save_activation_receiver, sender=User)
