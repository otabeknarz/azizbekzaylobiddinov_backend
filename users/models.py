import random

from django.db import models
from django.contrib.auth.models import AbstractUser


def generate_id() -> str:
    return str(random.randint(100000000, 999999999))


class User(AbstractUser):
    id = models.CharField(
        verbose_name='Telegram ID',
        max_length=20,
        unique=True,
        db_index=True,
        primary_key=True,
        default=generate_id
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=30,
        unique=True,
        db_index=True
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.id
        super(User, self).save(*args, **kwargs)
