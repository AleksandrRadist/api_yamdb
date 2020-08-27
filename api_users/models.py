from django.contrib.auth.models import AbstractUser
from django.db import models


class Role():
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )


class User(AbstractUser):
    bio = models.TextField(blank=True)
    role = models.CharField(
      max_length=25,
      choices=Role.ROLE_CHOICES,
      default=Role.USER
    )

    @property
    def is_admin(self):
        return self.role == Role.ADMIN and self.is_staff
