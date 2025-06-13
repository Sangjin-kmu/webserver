
from django.contrib import admin
from django.urls import path
from common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),
    path('add/', views.book_add, name='book_add'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('request-info/', views.request_info_view, name='request_info'),
    path('signup/', views.signup_view, name='signup'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
