# 웹서버컴퓨팅 20213039 이상진
## 과제9  

### 과제 결과 화면  
  
**전체 책 목록**  
<img width="346" alt="스크린샷 2025-05-22 오전 10 41 14" src="https://github.com/user-attachments/assets/66547d83-c44e-4d4c-a5f2-f2e2e5c98b42" />  
  
**특정 책의 대출 이력 확인(대출 이력이 없는 경우)**  
<img width="380" alt="스크린샷 2025-05-22 오전 10 41 20" src="https://github.com/user-attachments/assets/71701c87-d116-4c7b-b435-f6f12326e92b" />  
  
**특정 책의 대출 이력 확인(대출 이력이 있는 경우)**  
<img width="390" alt="스크린샷 2025-05-22 오전 10 41 09" src="https://github.com/user-attachments/assets/8b4e70f3-673d-48ce-9564-7ea2590ef2c8" />  
  
**단위 테스트 결과 성공 화면**  
<img width="566" alt="스크린샷 2025-05-22 오전 10 42 18" src="https://github.com/user-attachments/assets/027d6117-d703-4d98-89d7-c33dafe6eed8" />  
  
### 코드 완성  
  
**뷰(View) 와 서비스(Service Layer) 분리 이점**  
  
서비스(Service) 코드  
  
```python
from library.models import Book, BorrowHistory
from django.shortcuts import get_object_or_404

def get_all_books():
  return Book.objects.all()
def get_book_by_id(book_id: int) -> Book:
  return get_object_or_404(Book, id=book_id)
def get_borrow_history_for_book(book: Book):
  return BorrowHistory.objects.filter(book=book)
```
  
뷰(View) 코드  
  
```python
from django.shortcuts import render
from library.services import book_service

def book_list(request):
  books = book_service.get_all_books() 
  return render(request, 'library/book_list.html', {'books': books})
def book_history(request, book_id):
  book = book_service.get_book_by_id(book_id)
  histories = book_service.get_borrow_history_for_book(book)
  return render(request, 'library/book_history.html', {
    'book': book,
    'histories': histories,
  })
```  
  
**뷰(View) 와 서비스(Service Layer) 분리 예제**  
  
library/urls 코드  
  
```python
from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
  path('books/', views.book_list, name='book_list'),
  path('books/<int:book_id>/history/', views.book_history, name='book_history'),
]
```  
  
config/urls 코드  
  
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')), 
]
```
  
뷰(View) 코드  
  
```python
from django.shortcuts import render
from library.services import book_service

def book_list(request):
  books = book_service.get_all_books() 
  return render(request, 'library/book_list.html', {'books': books})
def book_history(request, book_id):
  book = book_service.get_book_by_id(book_id)
  histories = book_service.get_borrow_history_for_book(book)
  return render(request, 'library/book_history.html', {
    'book': book,
    'histories': histories,
```  
  
템플릿 코드(book_list.html)  
  
```html
<h1>📚 책 목록</h1>
<ul>
  {% for book in books %}
    <li>
      <a href="{% url 'library:book_history' book.id %}"> 
       {{ book.title }} by {{ book.author }}
      </a>
    </li>
  {% empty %}
    <li>등록된 책이 없습니다.</li>
  {% endfor %}
</ul>
```
  
템플릿 코드(book_history.html)  
  
```html
<h2>📖 대출 이력: {{ book.title }}</h2>
<ul>
  {% for history in histories %}
    <li>
      {{ history.user.username }} - {{ history.borrowed_at|date:"Y-m-d H:i" }}
      {% if history.returned_at %}
        (반납: {{ history.returned_at|date:"Y-m-d" }})
      {% else %}
        🕒 미반납
      {% endif %}
    </li>
  {% empty %}
    <li>대출 이력이 없습니다.</li>
  {% endfor %}
</ul>
<a href="{% url 'library:book_list' %}">← 책 목록으로</a> 
```  
  
**예외 처리 포함 서비스 함수**  
  
서비스 레이어 예제 코드  
  
```python
from library.models import Book
from library.exceptions import BookNotFound, BookHasNoBorrowHistory

def get_book_by_id(book_id: int) -> Book:
  try:
    return Book.objects.get(id=book_id)
  except Book.DoesNotExist:
    raise BookNotFound(f"ID {book_id}에 해당하는 책이 없습니다.")
def get_borrow_history_for_book(book: Book):
  histories = book.borrow_history.order_by('-borrowed_at')
  if not histories.exists():
    raise BookHasNoBorrowHistory(f"'{book.title}' 도서에는 대출 이력이 없습니다.")
  return histories
```
  
뷰 예제에서의 예외 처리 코드  
  
```python
from django.shortcuts import render
from django.http import HttpResponseNotFound
from library.services import book_service
from library.exceptions import BookNotFound, BookHasNoBorrowHistory

def book_history(request, book_id):
  try:
    book = book_service.get_book_by_id(book_id)
    histories = book_service.get_borrow_history_for_book(book)
  except BookNotFound as e:
    return HttpResponseNotFound(str(e))
  except BookHasNoBorrowHistory as e:
    return render(request, 'library/no_history.html', {'book': book, 'message': str(e)})
  return render(request, 'library/book_history.html', {
    'book': book,
    'histories': histories,
  })
```  
  
**단위 테스트**  
  
단위 테스트 코드  
  
```python
import pytest
from library.models import Book
from library.services.book_service import get_book_by_id
from library.exceptions import BookNotFound

@pytest.mark.django_db
def test_get_book_by_id_success():

  book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123')

  result = get_book_by_id(book.id)

  assert result == book
  assert result.title == 'Test Book'

@pytest.mark.django_db
def test_get_book_by_id_not_found():

  with pytest.raises(BookNotFound) as exc_info:
    get_book_by_id(9999)
  assert "ID 9999에 해당하는 책이 없습니다." in str(exc_info.value)
```  
  
단위 테스트 코드2  
  
```python
import pytest
from django.contrib.auth.models import User
from library.models import Book, BorrowHistory
from library.services.book_service import get_borrow_history_for_book
from library.exceptions import BookHasNoBorrowHistory

@pytest.mark.django_db
def test_get_borrow_history_for_book_success():

  user = User.objects.create(username='testuser') 
  book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123') 
  BorrowHistory.objects.create(book=book, user=user) 
  histories = get_borrow_history_for_book(book)

  assert histories.count() == 1 
  assert histories.first().user == user
@pytest.mark.django_db
def test_get_borrow_history_for_book_no_history():

  book = Book.objects.create(title='Empty Book', author='Nobody', isbn='9999999999999')

  with pytest.raises(BookHasNoBorrowHistory) as exc_info: 
    get_borrow_history_for_book(book) 
  assert "도서에는 대출 이력이 없습니다." in str(exc_info.value)
```
  
  
