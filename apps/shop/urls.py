from django.urls import path
from .views import (
    BookViewSet,
    BookRowViewSet,
    OnlyPrefetchReletedBookViewSet,
    OnlySelectReletedBookViewSet,
)

urlpatterns = [
    path("books/all/", BookViewSet.as_view({"get": "list"})),
    path("books/row/", BookRowViewSet.as_view({"get": "list"})),
    path("books/select/", OnlySelectReletedBookViewSet.as_view({"get": "list"})),
    path("books/prefetch/", OnlyPrefetchReletedBookViewSet.as_view({"get": "list"})),
]
