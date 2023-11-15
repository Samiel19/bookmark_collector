from rest_framework import serializers
from user.models import BookmarkUser


class BookmarkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmarkUser
        fields = (
            "id",
            "email",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}
