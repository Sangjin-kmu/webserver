
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Book
from django import forms



# ---------- Book 등록 폼 ----------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# ---------- 책 목록/추가 ----------
def book_list(request):
    keyword = request.GET.get('q', '')
    order = request.GET.get('order', '')
    books = Book.get_all_books()
    if keyword:
        books = Book.get_books_by_title_keyword(keyword)
    if order == 'title':
        books = books.order_by('title')
    return render(request, 'book_list.html', {'books': books, 'keyword': keyword, 'order': order})

def book_add(request):
    if not request.user.is_authenticated:
        return render(request, 'book_add.html', {'not_logged_in': True})

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'book_add.html', {'form': form})


# ---------- 로그인 관련 ----------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    return render(request, 'login.html')

@login_required
def home_view(request):
    return render(request, 'home.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 가입 후 자동 로그인
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# ---------- request info ----------
def request_info_view(request):
    context = {
        'method': request.method,
        'get_data': request.GET,
        'post_data': request.POST,
        'user': request.user,
        'is_logged_in': request.user.is_authenticated,
        'session_value': request.session.get('demo', '없음'),
        'user_agent': request.META.get('HTTP_USER_AGENT', '알 수 없음'),
        'client_ip': request.META.get('REMOTE_ADDR', '알 수 없음'),
        'path': request.path,
        'full_url': request.build_absolute_uri()
    }
    request.session['demo'] = '세션에서 저장한 값입니다.'
    return render(request, 'request_info.html', context)
