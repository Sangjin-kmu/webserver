from django.db import models
from django.db.models import QuerySet

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  
  def __str__(self):
    return f"{self.title} by {self.author}"
  
  @classmethod
  def get_all_books(cls) -> QuerySet['Book']:
    return cls.objects.all()
  
  @classmethod
  def get_all_books(cls) -> QuerySet['Book']: # --> 여기에 동작 코드를 작성하세요(1점)
    """
    전체 책 목록 반환
    """
    return cls.objects.all()# --> 여기에 동작 코드를 작성하세요(2점)
  
  @classmethod
  def get_books_by_author(cls, author_name) -> QuerySet['Book']: # -->여기 괄호안에 동작 코드를 작성하세요(1점)
    """
   특정 저자의 책만 반환
    """
    return cls.objects.filter(author__iexact = author_name) # --> 여기 괄호안에 동작 코드를 작성하세요(2점)
  @classmethod
  def get_books_by_title_keyword(cls, keyword) -> QuerySet['Book']: # --> 여기 괄호안에 동작 코드를 작성하세요(1점)
    """
    제목에 키워드가 포함된 책 반환 (대소문자 구분 없이)
    """
    return cls.objects.filter(title__icontains = keyword) # --> 여기에 동작 코드를 작성하세요(2점)
  @classmethod
  def get_books_ordered_by_title(cls) -> QuerySet['Book']: # --> 여기 괄호안에동작 코드를 작성하세요(1점)
    """
    제목 순으로 정렬된 책 목록 반환
    """
    return cls.objects.all().order_by('title') # --> 여기 괄호안에 동작 코드를 작성하세요(2점) 
