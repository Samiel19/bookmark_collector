from django.contrib import admin

from .models import Bookmark, Collection


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "id",
        "link",
        "created_at",
        "title",
        "type",
        "description",
        "image",
    )
    search_fields = (
        "author",
        "link",
        "created_at",
    )
    list_filter = (
        "author",
        "link",
        "created_at",
    )


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "id",
        "name",
        "created_at",
    )
    search_fields = (
        "author",
        "name",
        "created_at",
    )
    list_filter = (
        "author",
        "name",
        "created_at",
    )
