from api.bookmarks.views import BookmarkViewSet, CollectionViewSet
from api.users.views import UserViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("bookmarks", BookmarkViewSet, basename="bookmarks")
router.register("collections", CollectionViewSet, basename="collections")
router.register("bookmark_users", UserViewSet, basename="bookmark_users")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include("djoser.urls")),  # Работа с пользователями
    path("api/", include("djoser.urls.authtoken")),  # Работа с токенами
]
