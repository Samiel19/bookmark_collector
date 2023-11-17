from bookmark.models import Bookmark, Collection
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for bookmarks.

    """

    author = SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        fields = "__all__"
        model = Bookmark

    def validate(self, data):
        link = self.initial_data.get("link")
        if link in Bookmark.objects.filter(
            author=self.context["request"].user
        ).values_list("link", flat=True):
            raise ValidationError("You have this bookmark already!")
        return data


class CollectionSerializer(serializers.ModelSerializer):
    """
    Serializer for collections. User can add to collection only his bookmark.

    """

    links = PrimaryKeyRelatedField(queryset=Bookmark.objects.all(), many=True)
    author = SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        fields = "__all__"
        model = Collection

    def validate_links(self, links):
        for link in links:
            if self.context["request"].user != link.author:
                raise serializers.ValidationError("It's not yours... ;)")
        return links

    def validate(self, data):
        name = self.initial_data.get("name")
        if name in Collection.objects.filter(
            author=self.context["request"].user
        ).values_list("name", flat=True):
            raise ValidationError("You have this collection already!")
        return data
