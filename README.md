# 웹서버컴퓨팅 20213039 이상진
## 과제6  

**수정한 request_info.html**    
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Request 실습</title>
</head>
<body>
  <h2>🔍 request 객체 실습</h2>
  <p><strong>요청 방식:</strong> {{ request.method }}</p> 
  <p><strong>요청 경로:</strong> {{ request.path }}</p> 
  <p><strong>전체 URL:</strong> {{ request.build_absolute_uri }}</p>
  <p><strong>클라이언트 IP:</strong> {{ request.META.REMOTE_ADDR }}</p> 
  <p><strong>User-Agent:</strong> {{ request.META.HTTP_USER_AGENT }}</p> 
  <hr>
  <h3>🧾 GET 요청 정보</h3>
  <pre>{{ request.GET }}</pre>
  <h3>🧾 POST 요청 정보</h3>
  <pre>{{ request.POST }}</pre>
  <hr>
  <h3>🙍 사용자 정보</h3>
  <p>로그인 여부: {{ is_logged_in }}</p> 
  {% if is_logged_in %}
    <p>사용자: {{ request.user }}</p>
  {% else %}
    <p>익명 사용자입니다.</p>
  {% endif %}
  <hr>
  <h3>📦 세션 데이터</h3>
  <p>session['demo']: {{ request.session }}</p> 
  <hr>
  <h3>📤 요청 테스트</h3>
  <form method="get">
    <input type="text" name="search" placeholder="GET 요청 파라미터">
    <button type="submit">GET 전송</button>
  </form>
  <form method="post">
    {% csrf_token %}
    <input type="text" name="message" placeholder="POST 요청 내용">
    <button type="submit">POST 전송</button>
  </form>
</body>
</html>
```  
  
**첫 실행화면**  
  
<img width="919" alt="스크린샷 2025-04-30 오후 1 56 29" src="https://github.com/user-attachments/assets/06ef6d12-b118-4615-8f8d-5c605ccc4c05" />  
  
**GET요청**  
GET으로 123을 요청 하였다.  
  
<img width="927" alt="스크린샷 2025-04-30 오후 1 56 38" src="https://github.com/user-attachments/assets/10627099-bf1a-4e92-a036-dcdd64782f22" />  
  
**POST요청**  
POST로 234를 요청 하였다.  
  
<img width="1015" alt="스크린샷 2025-04-30 오후 1 56 57" src="https://github.com/user-attachments/assets/572cb871-1ffd-44d1-88d6-94b78ab702e6" />  

**수정한 upload_file.html**
  
```html
<h2>📤 파일 업로드</h2>
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  <label>제목:</label><br>
  <input type="text" name="title"><br><br>
  <label>파일 선택:</label><br>
  <input type="file" name="file"><br><br>
  <button type="submit">업로드</button>
</form>
{% if uploaded_file_url %} 
  <h3>업로드 결과</h3>
  <p><strong>제목:</strong> {{ title }}</p>
  <p><a href="{{ uploaded_file_url }}">업로드된 파일 보기</a></p>
{% endif %}
def login_view(request):
  if request.method == 'POST':
    username = request.POST['username'] # 여기에 동작코드를 작성하세요(1점)
    password = request.POST['password'] # 여기에 동작코드를 작성하세요(1점)
    user = authenticate(request, username=username, password=password) # 여기에동작코드를 작성하세요(총 2점,각 1점)
    if user is not None:
      login(request, user) # 여기에 동작코드를 작성하세요(1점)
      return redirect('home') # 여기에 동작코드를 작성하세요(1점)
    else:
      messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
  return render(request, 'accounts/login.html') # 여기에 동작코드를 작성하세요(1점)
@login_required
def home_view(request):
  return render(request, 'accounts/home.html', {'user': request.user})
def logout_view(request):
  logout(request) # 여기에 동작코드를 작성하세요(1점)
  return redirect('login')
```

**수정한 views.py**  

```python
from django.shortcuts import render
from .models import UploadedFile
from django.urls import path
from . import views

def file_upload_view(request):
  uploaded_file_url = None
  title = None
  if request.method == 'POST' and request.FILES.get('file'):
    file = request.FILES['file'] 
    title = request.POST.get('title', '')
    uploaded = UploadedFile.objects.create(title=title, file=file)
    uploaded_file_url = uploaded.file.url
  return render(request, 'request_test/upload_file.html', {
    'uploaded_file_url': uploaded_file_url,
    'title': title
  })
urlpatterns = [
    path('login/', views.login_view, name='login'), # 여기에 동작코드를 작성하세요(1점)
    path('logout/', views.logout_view, name='logout'), # 여기에 동작코드를 작성하세요(1점)
    path('home/', views.home_view, name='home'), # 여기에 동작코드를 작성하세요(1점)
]
```

**파일 업로드 화면**  
  
<img width="398" alt="스크린샷 2025-04-30 오후 1 55 45" src="https://github.com/user-attachments/assets/de09830c-eb85-4ea0-aeab-111ac83c253d" />  

깃허브 주소 : https://github.com/Sangjin-kmu/webserver/tree/request-info
  
