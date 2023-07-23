from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(blank=False, null=False, unique=True)
