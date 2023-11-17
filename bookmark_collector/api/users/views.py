from api.permissions import AdminOrReadOnly
from rest_framework import permissions, viewsets
from user.models import BookmarkUser

from .serializers import BookmarkUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Return bookmark_coolector users.

    """

    serializer_class = BookmarkUserSerializer
    queryset = BookmarkUser.objects.all()
    permission_classes = (AdminOrReadOnly, permissions.IsAuthenticated)
