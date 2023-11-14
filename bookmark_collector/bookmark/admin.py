from django.contrib import admin

from .models import Bookmark, Collection


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "link",
        "created_at",
        "title",
        "type",
        "description",
        "image",
    )
    search_fields = (
        "link",
        "created_at",
    )
    list_filter = (
        "link",
        "created_at",
    )


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    search_fields = (
        "name",
        "created_at",
    )
    list_filter = (
        "name",
        "created_at",
    )
