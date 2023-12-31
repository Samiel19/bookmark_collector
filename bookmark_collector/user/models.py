from core.enums import Limits
from django.contrib.auth.models import AbstractUser
from django.db import models


class BookmarkUser(AbstractUser):
    """Model describing User"""

    email = models.EmailField(
        "email", unique=True, max_length=Limits.EMAIL_MAX_LEN.value
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("-date_joined",)

    def __str__(self):
        return f"User {self.email}"
