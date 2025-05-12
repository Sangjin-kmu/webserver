# 웹서버컴퓨팅 20213039 이상진
## 과제8

**수정한 myapp/view.py**  
  
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# @api_view(['GET'])
# def hello_api(request):
#    return Response({"message": "안녕하세요, DRF API입니다!"})

@api_view(['POST'])
def receive_post(request):
  name = request.data.get('name')
  message = request.data.get('message')
 
  if not name or not message:
    return Response(
      {"error": "name과 message는 필수입니다."},
      status=status.HTTP_400_BAD_REQUEST # <-- 여기에 동작코드를 작성하세요(2점)
    )
  return Response(
   {"result": f"{name}님이 보낸 메시지: {message}"},
    status=status.HTTP_201_CREATED # <-- 여기에 동작코드를 작성하세요(2점)
  )

```

**수정한 myapp/urls.py**  
  
```python
from django.urls import path
# from .views import hello_api

# urlpatterns = [
#   path('hello/', hello_api),
# ]

from .views import receive_post

urlpatterns = [
  path('post/', receive_post), # <-- 여기에 동작코드를 작성하세요(2점)
]
```  
  
  
**정상 응답**  

  <img width="1194" alt="스크린샷 2025-05-12 오후 2 01 51" src="https://github.com/user-attachments/assets/0f936684-6966-485d-a785-6d37e47c30c5" />  

HTTP 201 Created가 뜨면서 정상적으로 내용이 나온다.  
  
**비정상 응답**  
  
  <img width="1175" alt="스크린샷 2025-05-12 오후 2 01 59" src="https://github.com/user-attachments/assets/dbc938a5-940b-4d5c-9aa6-476cce179d68" />  
  
HTTP 400 Bad Request가 뜨면서 name 과 message를 입력하라고 나온다.  
  
깃허브 주소 : https://github.com/Sangjin-kmu/webserver/tree/post
