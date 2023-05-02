import uuid

from django.db import models
from django.conf import settings

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

import model_helpers


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, client_name, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(client_name, email, password, **other_fields)

    def create_user(self, client_name, email, password, **other_fields):

        if not client_name:
            raise ValueError(_('You must provide user name'))
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, client_name=client_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class ClientProfile(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(_('email address'), unique=True)
    client_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    business_name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    charge_amount_per_job_post = models.FloatField(
        max_length=10, null=True, blank=True)

    country = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    zone = models.CharField(max_length=100, null=True, blank=True)
    woreda = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)

    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['client_name', 'phone']

    def __str__(self):
        return f'{self.client_name} Profile'


class ApplicantProfile(models.Model):

    phone = models.BigIntegerField(primary_key=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    applicant_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    data_of_birth = models.DateTimeField(null=True, blank=True)

    interested_in = models.CharField(max_length=255, null=True, blank=True)
    class_of = models.IntegerField(null=True, blank=True)
    cv_file = models.FileField(null=True, blank=True,
                               upload_to=model_helpers.upload_to)

    phone = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    zone = models.CharField(max_length=100, null=True, blank=True)
    woreda = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)

    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['applicant_name', 'email', 'phone']

    def __str__(self):
        return f'{self.client_name} Profile'
