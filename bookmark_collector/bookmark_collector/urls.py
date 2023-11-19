from api.bookmarks.views import BookmarkViewSet, CollectionViewSet
from api.users.views import UserViewSet
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
    openapi.Info(
        title="Bookmark collector API",
        default_version="v1",
        description="Documentation for Bookmark collector app",
        contact=openapi.Contact(email="anton.sadagov@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register("bookmarks", BookmarkViewSet, basename="bookmarks")
router.register("collections", CollectionViewSet, basename="collections")
router.register("bookmark_users", UserViewSet, basename="bookmark_users")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include("djoser.urls")),
    path("api/", include("djoser.urls.authtoken")),
]


urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
