from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Author, Publisher, UserBookRelation
from .serializers import BookSerializer
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 1000
    page_query_param = "p"


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("publisher").prefetch_related("author").all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination


class BookRowViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination


class OnlySelectReletedBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("publisher").all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination


class OnlyPrefetchReletedBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.prefetch_related("author").all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination
