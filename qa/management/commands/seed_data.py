import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from qa.models import Question, Answer
from faker import Faker

class Command(BaseCommand):
  help = 'Create test users, questions, and answers'
  def handle(self, *args, **kwargs):
    fake = Faker()

    # 사용자 생성
    for i in range(5):
      username = f'user{i+1}'
      if not User.objects.filter(username=username).exists():
       User.objects.create_user(username=username, password='test1234')
       self.stdout.write(f"Created user: {username}")
    users = list(User.objects.all())

    # 질문 생성
    for _ in range(10):
      author = random.choice(users)
      q = Question.objects.create(
       title=fake.sentence(),
       content=fake.paragraph(),
       author=author
      )
      self.stdout.write(f"Created question: {q.title}")
    
      # 답변 생성
    for _ in range(random.randint(1, 3)):
     Answer.objects.create(
     question=q,
      content=fake.paragraph(),
      author=random.choice(users)
    )
    self.stdout.write(f" -> Added answer")