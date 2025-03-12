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

