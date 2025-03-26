from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"Answer to {self.question.title} by {self.author.username}"