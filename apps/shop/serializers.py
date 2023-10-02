from rest_framework import serializers
from .models import Publisher, Author, Book


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=60)
    state_province = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=50)
    website = serializers.URLField()

    class Meta:
        model = Publisher
        fields = "__all__"


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=40)
    email = serializers.EmailField()

    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = AuthorSerializer(many=True)
    publisher = serializers.CharField()
    publication_date = serializers.DateTimeField()

    class Meta:
        model = Book
        fields = ("title", "author", "publisher", "publication_date")
