# webserver

Model 통하여 pybo를 만들어서 띄워보면, Page not found가 뜬다.  
그 이유는 우리가 페이지를 요청하면 가장먼저 urls.py파일이 호출된다.   
그래서 urls.py 랑 view.py를 매핑시키지 않으면, view.py안의 내용을 받아오지 못해.   
Page not found 가 뜬다.  
그래서 urls.py 코드속 urlpatterns을 통해 pybo의 views.py를 매핑 시켜주어야한다.     

```python
path(’pybo/’, views.index, name=’index’)
```
