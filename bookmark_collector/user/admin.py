from django.contrib import admin
from user.models import BookmarkUser


@admin.register(BookmarkUser)
class BookmarkUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
    )
    search_fields = ("email", "date_joined")
    list_filter = ("date_joined",)
