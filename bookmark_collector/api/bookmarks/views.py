from api.permissions import IsAuthorOrReadOnlyPermission
from bookmark.models import Bookmark, Collection
from rest_framework import viewsets

from .serializers import BookmarkSerializer, CollectionSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Bookmark.objects.filter(author=self.request.user)


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Collection.objects.filter(author=self.request.user)
