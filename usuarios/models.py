from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.get_full_name()