import core.funks as f
from core.enums import Limits
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Bookmark(models.Model):
    """Model describing bookmarks"""

    link = models.URLField(
        "Ссылка",
        unique=True,
        max_length=Limits.URL_LEN.value,
        help_text="Ссылка",
    )
    title = models.CharField(
        "Название",
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        blank=True,
        help_text="Название закладки",
        editable=False,
    )
    type = models.CharField(
        "Тип",
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        blank=True,
        help_text="Тип закладки",
        editable=False,
    )
    description = models.TextField(
        "Описание",
        blank=True,
        help_text="Описание закладки",
        editable=False,
    )
    image = models.URLField(
        "Изображение",
        max_length=Limits.URL_LEN.value,
        blank=True,
        editable=False,
    )
    created_at = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True,
        editable=False,
    )
    updated = models.DateTimeField("updated", auto_now=True)

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
        ordering = ("created_at",)

    @property
    def get_title(self):
        return f.soup_maker(self.link, "title")

    @property
    def get_type(self):
        return f.soup_maker(self.link, "type")

    @property
    def get_description(self):
        return f.soup_maker(self.link, "description")

    @property
    def get_image(self):
        return f.soup_maker(self.link, "image")

    def save(self, *args, **kwarg):
        self.title = self.get_title
        self.type = self.get_type
        self.description = self.get_description
        self.image = self.get_image
        super(Bookmark, self).save(*args, **kwarg)

    def __str__(self):
        return f"Закладка {self.link}"


class Collection(models.Model):
    """Model describing bookmark collections"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец коллекции",
        db_index=True,
    )
    link = models.ManyToManyField(
        Bookmark,
        verbose_name="Закладка",
        blank=True,
    )
    updated = models.DateTimeField("updated", auto_now=True)
    created_at = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True,
        editable=False,
    )
    name = models.CharField(
        "Имя коллекции",
        unique=True,
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        help_text="Название коллекции закладок",
    )
    description = models.CharField(
        "Описание коллекции",
        max_length=Limits.TEXT_MAX_LEN.value,
        help_text="Описание коллекции закладок",
    )

    class Meta:
        default_related_name = "collection"
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
        ordering = ("-created_at",)

    def __str__(self):
        return f"Коллекция закладок {self.name} пользователя {self.author}"
