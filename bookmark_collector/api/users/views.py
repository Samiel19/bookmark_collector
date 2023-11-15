from api.permissions import AdminOrReadOnly
from rest_framework import viewsets
from user.models import BookmarkUser

from .serializers import BookmarkUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkUserSerializer
    queryset = BookmarkUser.objects.all()
    permission_classes = (AdminOrReadOnly,)
