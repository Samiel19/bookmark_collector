import core.funcs as f
from core.enums import Limits
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Bookmark(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Bookmark author",
        db_index=True,
    )
    link = models.URLField(
        "URL",
        max_length=Limits.URL_LEN.value,
        help_text="Bookmark URL",
    )
    title = models.CharField(
        "Name",
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        blank=True,
        help_text="Bookmark",
        editable=False,
    )
    type = models.CharField(
        "Type",
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        blank=True,
        help_text="Bookmark type",
        editable=False,
    )
    description = models.TextField(
        "Description",
        blank=True,
        help_text="Bookmark description",
        editable=False,
    )
    image = models.URLField(
        "Image",
        max_length=Limits.URL_LEN.value,
        blank=True,
        editable=False,
        db_column="image",
    )
    created_at = models.DateTimeField(
        "Publication date",
        auto_now_add=True,
        editable=False,
    )
    updated = models.DateTimeField("updated", auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "link"],
                name="unique_link",
                violation_error_message="You have this link already!",
            ),
        ]
        verbose_name = "Bookmark"
        verbose_name_plural = "Bookmarks"
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
        return f"Bookmark {self.link}"


class Collection(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Collection owner",
        db_index=True,
    )
    links = models.ManyToManyField(
        Bookmark,
        verbose_name="Bookmark",
        blank=True,
    )
    updated = models.DateTimeField("updated", auto_now=True)
    created_at = models.DateTimeField(
        "Publication date",
        auto_now_add=True,
        editable=False,
    )
    name = models.CharField(
        "Collection name",
        max_length=Limits.USER_MODEL_MAX_LEN.value,
        help_text="Bookmarks collection name",
    )
    description = models.CharField(
        "Collection description",
        max_length=Limits.TEXT_MAX_LEN.value,
        help_text="Bookmarks collection description",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "name"],
                name="unique_collection",
                violation_error_message="You have this collection already!",
            ),
        ]
        default_related_name = "collection"
        verbose_name = "Collection"
        verbose_name_plural = "Collections"
        ordering = ("-created_at",)

    def __str__(self):
        return f"Bookmarks collection {self.name} of user {self.author}"
