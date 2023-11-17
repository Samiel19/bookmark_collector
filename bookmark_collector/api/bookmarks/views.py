from api.permissions import IsAuthorOrReadOnlyPermission
from bookmark.models import Bookmark, Collection
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .serializers import BookmarkSerializer, CollectionSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    """
    GET - Return user's bookmarks for DB.
    POST - Creating new bookmark. Bookmark must be unique for user.

    """

    serializer_class = BookmarkSerializer
    permission_classes = (
        IsAuthorOrReadOnlyPermission,
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Bookmark.objects.filter(author=self.request.user)


class CollectionViewSet(viewsets.ModelViewSet):
    """
    GET - Return user's collections for DB.
    POST - Creating new collection. Collection's name must be unique for user.
    User can add only this user's bookmarks

    """

    serializer_class = CollectionSerializer
    permission_classes = (
        IsAuthorOrReadOnlyPermission,
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Collection.objects.filter(author=self.request.user)
