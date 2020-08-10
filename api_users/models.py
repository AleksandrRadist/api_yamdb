from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_ROLE_CHOICES = (
      ('user', 'user'),
      ('moderator', 'moderator'),
      ('admin', 'admin'),
    )

    bio = models.TextField(blank=True)
    role = models.CharField(
      max_length=20,
      choices=USER_ROLE_CHOICES,
      default='user'
    )
    is_staff = models.BooleanField(default=False)
