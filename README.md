# 웹서버컴퓨팅 20213039 이상진
## 과제1

Model 통하여 pybo를 만들어서 띄워보면, Page not found가 뜬다.  
그 이유는 우리가 페이지를 요청하면 가장먼저 urls.py파일이 호출된다.   
그래서 urls.py 랑 view.py를 매핑시키지 않으면, view.py안의 내용을 받아오지 못해.   
Page not found 가 뜬다.  
<img width="266" src="https://github.com/user-attachments/assets/05111cd1-abe3-40bf-8837-82fc6e8c82a6" />  

그래서 urls.py 코드속 urlpatterns을 통해 pybo의 views.py를 매핑 시켜주어야한다.     

```python
path(’pybo/’, views.index, name=’index’)
```
위 코드를 해석해보면 'pybo/'는 url입력으로 발생하는 이벤트이고,  
views.index, name='index'는 views.py의 index함수를 처리 해주는 이벤트 핸들러이다.  
그것을 path함수를 이용해 매핑시켜주고 있는 것이다.  

<img width="532" alt="스크린샷 2025-03-12 오후 2 31 25" src="https://github.com/user-attachments/assets/62cce99d-6b29-413d-ba76-8e39022fa16d" />  

과제에 나온 <수정할 문제 코드>가 해당부분까지 완료한 상태이다.   
하지만 urls.py파일은 views.py파일의 위치를 모르기 때문에   

```python
from pybo import views
```
해당 코드를 추가해 import해주면 문제가 없어진다.  


결과 화면  
<img width="438" alt="스크린샷 2025-03-12 오후 2 34 35" src="https://github.com/user-attachments/assets/3c345cab-8be9-4a5f-b4bc-7104185516c6" />  


## 과제2  

config urls.py 과제 코드  
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
]
```  
lpybo views.py 과제 코드
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
```

해당 과제코드를 보면 include('pybo.urls')를 통해 pybo파일의 urls.py파일을 따른다는 뜻이다.  
그래서 pybo에서 urls.py의 파일을 열어보면  

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]

```  
이런식으로 config에 사용할 코드를 각 사이트에 맞게 전담해서 분배할수있게 만들 수 있다.  
그래서 실행하면 아래 사진처럼 127.0.0.1:8000/pybo/ 사이트에선 문제 없이 잘뜬다.  
<img width="350" alt="image" src="https://github.com/user-attachments/assets/3a4504b1-53a4-429d-9bb9-a1ea769c518f" />

하지만 과제에서 요구하는 내용은 /pybo/가 안붙은 127.0.0.1:8000에서도 해당 views의 내용을 볼수있는 방법을 구해야한다.  
<img width="641" alt="image" src="https://github.com/user-attachments/assets/8163ce2b-1a22-45f8-bf86-86fc633c803b" />

수업때 배운 간단한 코드 한줄만 추가하면 쉽게 해결이 된다.
```python
path('', views.index),
```  
config urls.py 의 urlpatterns 에 해당 코드를 추가한다. 하지만 추가만 하면 views의 index 내용을 읽을 수 없으니,  
```python
from pybo import views
```
해당 코드를 통해 views.py 파일 코드를 가져와야한다.  
그래서 최종완성 코드는 아래 처럼 나온다.  
```python
from django.contrib import admin
from django.urls import include, path
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), # include를 통해 전담 URL로 가라.
    path('', views.index),
]
```
 ![image](https://github.com/user-attachments/assets/515a4c3f-0da8-410e-9ee4-675bfd889df6)

사진 처럼 문제 없이 두 주소다 내용이 뜬다.  

## 과제3  

**로그인 전 127.0.0.1:8020 화면**  
  
<img width="1149" alt="스크린샷 2025-03-26 오후 2 17 03" src="https://github.com/user-attachments/assets/ed650896-a46c-404b-93e7-5f7ac4865f69" />  
  
**user1 / test1234 로 로그인 후 127.0.0.1:8020 화면**  
  
<img width="1149" alt="스크린샷 2025-03-26 오후 2 16 49" src="https://github.com/user-attachments/assets/4bd7acae-809a-4818-b5cd-79168ab9da8a" />
  
**여기서 과제에 주어진 코드만 이용하면 로그인시 127.0.0.1:8020/account/profile 주소로 넘어가고 logout을 하면 어드민(관리자) 페이지로 넘어가는 버그가 있다.**  
  
로그인  
<img width="1063" alt="스크린샷 2025-03-26 오후 2 35 48" src="https://github.com/user-attachments/assets/c7e566d2-a303-4397-9983-54bf9d603029" />  
  
로그아웃  
<img width="392" alt="스크린샷 2025-03-26 오후 2 35 28" src="https://github.com/user-attachments/assets/e40dcaf3-d3a5-4e0d-bbf0-4ee077669f15" />  
  
**그래서 qna_site/setting.py 에 2줄을 추가하여 로그인 로그아웃시 바로 127.0.0.1:8020으로 넘어가게 코드를 수정하였다.**  
  
  <img width="283" alt="스크린샷 2025-03-26 오후 2 37 25" src="https://github.com/user-attachments/assets/318604a5-6844-49ab-b778-4b9032b18402" />  
  
```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```
  
**깃허브 코드 화면**  
  
<img width="1068" alt="스크린샷 2025-03-26 오후 1 44 12" src="https://github.com/user-attachments/assets/a0534c98-4842-457d-9241-59af46ea8b0d" />  
  
### 노션에는 어떤걸 코드를 업로드 하는지 몰라 모든 코드 파일을 업로드 및 질문목록 Bootstrap 카드(Card) 스타일로 정리한 코드도 따로 업로드 하였습니다.  

  
**노션 코드 업로드 화면**  
  
<img width="1119" alt="스크린샷 2025-03-26 오후 2 18 26" src="https://github.com/user-attachments/assets/8bc01c83-1adf-4352-aa4f-9e3a2d38405d" />  
  
**노션 질문목록 Bootstrap 카드(Card) 스타일로 정리 코드 화면**  
  
 <img width="1118" alt="스크린샷 2025-03-26 오후 2 25 14" src="https://github.com/user-attachments/assets/a50c7c82-57da-48a9-b4bf-2b131e45eb0f" />  
 
깃허브 주소 : https://github.com/Sangjin-kmu/webserver  
노션 주소 : https://www.notion.so/20213039-3-1c0103a1286a80d195f6c9a0b738b7b7 

## 과제4  

@csrf_exempt를 사용하지 않을 때의 웹사이트 결과 화면 캡쳐   
   
```python
@login_required
# @csrf_exempt
def write_post(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    Post.objects.create(
      author=request.user,
      title=title,
      content=content
 )
    return HttpResponse("게시글 작성 완료")
  return render(request, 'write.html')
```   

  <img width="967" alt="스크린샷 2025-03-31 오후 2 32 46" src="https://github.com/user-attachments/assets/1acc395b-18dd-453b-805d-64f8f3b04384" />  

  사진처럼 Forbidden (403)이 뜨고 **CSRF 검증에 실패했습니다. 요청을 중단하였습니다.** 가 뜨는걸 확인할 수 있다.  
  (한국어로 바꿔나서 과제자료랑 다르게 한국어로 표시)  

@csrf_exempt를 사용할 때 웹사이트 결과 화면 캡쳐   
```python
@login_required
@csrf_exempt
def write_post(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    Post.objects.create(
      author=request.user,
      title=title,
      content=content
 )
    return HttpResponse("게시글 작성 완료")
  return render(request, 'write.html')
```

  <img width="470" alt="스크린샷 2025-03-31 오후 2 33 09" src="https://github.com/user-attachments/assets/3588b110-79a4-4d19-a915-f84b63947a00" />  

사진처럼 127.0.0.1:8000/attack/ 에 접속하였을때 정상적으로 글이 작성되었다고 뜬다.  
그럼 관리자 사이트를 통해 작성한 글 리스트를 확인.  
  
<img width="840" alt="스크린샷 2025-03-31 오후 2 34 23" src="https://github.com/user-attachments/assets/919d425f-e728-43c5-8bc0-100a2f2adc07" />  

사진 처럼 내가 작성한 글외에 공격 제목이라는 타이틀을 가진 글들이 생성되었다.  
그럼 저 글을 클릭해서 내용을 보면  

<img width="962" alt="스크린샷 2025-03-31 오후 2 35 02" src="https://github.com/user-attachments/assets/f29703c7-be9d-4442-9db9-1d9547133c67" />  
  
해당사진 처럼 공격자가 강제로 작성한 글입니다. 라고 적혀있는걸 확인할 수 있다.  


  깃허브 주소 : https://github.com/Sangjin-kmu/webserver/tree/csrf

## 과제4  

**books/models.py 코드 수정**  
  
```python
from django.db import models
from django.db.models import QuerySet

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  
  def __str__(self):
    return f"{self.title} by {self.author}"
  
  @classmethod
  def get_all_books(cls) -> QuerySet['Book']: 
    """
    전체 책 목록 반환
    """
    return cls.objects.all()
  
  @classmethod
  def get_books_by_author(cls, author_name) -> QuerySet['Book']: 
    """
   특정 저자의 책만 반환
    """
    return cls.objects.filter(author__iexact = author_name) 
  @classmethod
  def get_books_by_title_keyword(cls, keyword) -> QuerySet['Book']:
    """
    제목에 키워드가 포함된 책 반환 (대소문자 구분 없이)
    """
    return cls.objects.filter(title__icontains = keyword)
  @classmethod
  def get_books_ordered_by_title(cls) -> QuerySet['Book']:
    """
    제목 순으로 정렬된 책 목록 반환
    """
    return cls.objects.all().order_by('title') 

```  
빈곳을 채워 넣은 후 코드  
  
**shell 사용예시 및 출력예시**  
  
1. 전체 책 조회  
<img width="282" alt="스크린샷 2025-04-09 오후 2 14 50" src="https://github.com/user-attachments/assets/13ec65a7-5475-4529-bad8-481880bcc721" />
  
2. 특정 저자 책만 조회  
<img width="444" alt="스크린샷 2025-04-09 오후 2 16 08" src="https://github.com/user-attachments/assets/8d0aec97-6eef-4014-9c97-bd210f9ec916" />
  
3. 제목 키워드로 검색  
<img width="442" alt="스크린샷 2025-04-09 오후 2 17 51" src="https://github.com/user-attachments/assets/02fd1bfb-d9c1-4ab2-b0cb-348ef6866a8e" />
  
4. 제목순 정렬  
<img width="379" alt="스크린샷 2025-04-09 오후 2 27 01" src="https://github.com/user-attachments/assets/d6f1ce48-42c7-4757-86c1-117b11dbaac8" />

  
  
깃허브 주소 : https://github.com/Sangjin-kmu/webserver/tree/book
