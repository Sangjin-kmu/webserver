# 웹서버컴퓨팅 20213039 이상진
## 과제7  

**수정한 accounts/view.py**  
  
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

**수정한 accouts/urls.py**  
  
```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'), # 여기에 동작코드를 작성하세요(1점)
    path('logout/', views.logout_view, name='logout'), # 여기에 동작코드를 작성하세요(1점)
    path('home/', views.home_view, name='home'), # 여기에 동작코드를 작성하세요(1점)
]
```
  
**로그인 화면**  

<img width="282" alt="스크린샷 2025-05-07 오후 2 10 48" src="https://github.com/user-attachments/assets/7716d53b-a1a8-4192-a27a-688828e7d1e8" />  
  
**실행화면**  

<img width="343" alt="스크린샷 2025-05-07 오후 2 12 33" src="https://github.com/user-attachments/assets/8571d51d-6530-4da1-a347-6c90b36594a8" />  
  
**로그아웃 화면**  

<img width="344" alt="스크린샷 2025-05-07 오후 2 12 42" src="https://github.com/user-attachments/assets/0e9aef2a-1508-445f-8adc-40a62eddb450" />  
  

깃허브 주소 : https://github.com/Sangjin-kmu/webserver/tree/login
