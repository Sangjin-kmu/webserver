from django.db import models
from django.db.models import QuerySet

# ---------- Book 모델 ----------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def get_all_books(cls) -> QuerySet['Book']:
        return cls.objects.all()

    @classmethod
    def get_books_by_author(cls, author_name: str) -> QuerySet['Book']:
        return cls.objects.filter(author__iexact=author_name)

    @classmethod
    def get_books_by_title_keyword(cls, keyword: str) -> QuerySet['Book']:
        return cls.objects.filter(title__icontains=keyword)

    @classmethod
    def get_books_ordered_by_title(cls) -> QuerySet['Book']:
        return cls.objects.all().order_by('title')