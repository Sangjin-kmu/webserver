from library.models import Book

class BookNotFound(Exception):
  """요청한 책이 존재하지 않을 경우"""
  pass
class BookHasNoBorrowHistory(Exception):
  """책에 대출 이력이 없을 경우"""
  pass
def get_book_by_id(book_id):
  try:
    return Book.objects.get(id=book_id)
  except Book.DoesNotExist:
    raise BookNotFound(f"책 ID {book_id}를 찾을 수 없습니다.")