from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Book, Comment, Rating
from .forms import CommentForm, RatingForm, BookForm

# ---------- 책 상세 ----------
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # 조회수 증가 세션 처리
    viewed_flag = f'viewed_book_{book_id}'
    if request.method == "GET" and not request.session.get(viewed_flag):
        book.increase_views()
        request.session[viewed_flag] = True

    comments = book.comments.all().order_by('-created_at')
    form = CommentForm()
    rating_form = None
    user_rating = None

    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(book=book, user=request.user).first()

        if request.method == "POST":
            if 'content' in request.POST:
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.book = book
                    comment.user = request.user
                    comment.save()
                    return redirect('book_detail', book_id=book.id)

            elif 'score' in request.POST:
                rating_form = RatingForm(request.POST)
                if rating_form.is_valid() and not user_rating:
                    rating = rating_form.save(commit=False)
                    rating.book = book
                    rating.user = request.user
                    rating.save()
                    return redirect('book_detail', book_id=book.id)
        else:
            rating_form = RatingForm()

    context = {
        'book': book,
        'form': form,
        'comments': comments,
        'avg_rating': book.get_average_rating(),
        'user_rating': user_rating,
        'rating_form': rating_form,
    }
    return render(request, 'book_detail.html', context)


# ---------- 책 목록 ----------
def book_list(request):
    keyword = request.GET.get('q', '')
    order = request.GET.get('order', '')
    books = Book.get_all_books()
    if keyword:
        books = Book.get_books_by_title_keyword(keyword)
    if order == 'title':
        books = books.order_by('title')
    return render(request, 'book_list.html', {'books': books, 'keyword': keyword, 'order': order})


# ✅ ---------- 책 등록 ----------
def book_add(request):
    if not request.user.is_authenticated:
        return render(request, 'book_add.html', {'not_logged_in': True})

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)  # ✅ 이미지 업로드 처리
        if form.is_valid():
            form.save()
            print("✅ 저장된 book 객체:", Book)
            print("📷 이미지 경로:", Book.image)
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'book_add.html', {'form': form})


# ---------- 로그인 ----------
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
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# ---------- 요청 정보 ----------
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
