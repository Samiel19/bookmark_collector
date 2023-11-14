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
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-date_joined",)

    def __str__(self):
        return f"Пользователь {self.email}"
