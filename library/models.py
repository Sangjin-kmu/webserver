# library/models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  isbn = models.CharField(max_length=20, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class BorrowHistory(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_history')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  borrowed_at = models.DateTimeField(auto_now_add=True)
  returned_at = models.DateTimeField(null=True, blank=True)

def __str__(self):
  return f"{self.user.username} - {self.book.title}"