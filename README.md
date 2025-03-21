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


