from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
  help = 'Insert sample books'
    
  def handle(self, *args, **kwargs):
    Book.objects.create(title='1984', author='George Orwell')
    Book.objects.create(title='Brave New World', author='Aldous Huxley')
    Book.objects.create(title='Fahrenheit 451', author='Ray Bradbury')
    self.stdout.write(self.style.SUCCESS('Sample books inserted!'))