from django.core.management.base import BaseCommand
from library.models import Book, BorrowHistory
from django.contrib.auth.models import User
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone
import datetime

class Command(BaseCommand):
  help = '랜덤 대출 이력을 생성합니다.'
  def add_arguments(self, parser):
    parser.add_argument('--total', type=int, default=50, help='생성할 대출기록 수')
  def handle(self, *args, **options):
    fake = Faker()
    books = list(Book.objects.all())
    users = list(User.objects.all())
    total = options['total']
    if not books or not users:
      self.stdout.write(self.style.ERROR("책과 사용자 데이터가 필요합니다."))
      return
    for _ in range(total):
      book = random.choice(books)
      user = random.choice(users)
      borrowed_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=datetime.timezone.utc)
      returned = random.choice([True, False])
      returned_at = borrowed_at + timedelta(days=random.randint(1, 30))
      if returned:
        BorrowHistory.objects.create(
          book=book,
          user=user,
          borrowed_at=borrowed_at,
          returned_at=returned_at
        )
      else:
        None
    self.stdout.write(self.style.SUCCESS(f"✅ 대출 기록 {total}개 생성 완료!"))