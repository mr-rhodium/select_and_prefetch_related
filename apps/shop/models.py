from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, "Ok"),
        (2, "Fine"),
        (3, "Good"),
        (4, "Amazing"),
        (5, "Incredible"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    class Meta:
        verbose_name = "User book relation"
        verbose_name_plural = "User book relations"

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    def get_book(self):
        return self.book


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "publisher"
        verbose_name_plural = "publishers"


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publication_date"]
        verbose_name = "book"
        verbose_name_plural = "books"
