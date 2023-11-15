from bookmark.models import Bookmark, Collection
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class BookmarkSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        fields = "__all__"
        model = Bookmark


class CollectionSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="email", read_only=True)
    # link = SlugRelatedField(slug_field='', read_only=True)

    class Meta:
        fields = "__all__"
        model = Collection

    """
        if self.context['request'].user == self.link.author:
            return link
        raise serializers.ValidationError("Как это к вам попало! ;)")"""
