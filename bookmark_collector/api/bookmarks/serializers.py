from bookmark.models import Bookmark, Collection
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
            print(link.author)
            if self.context["request"].user != link.author:
                raise serializers.ValidationError("It's not your.... ;)")
        return links
