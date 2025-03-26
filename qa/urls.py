from django.urls import path
from . import views

urlpatterns = [
  path('', views.question_list, name='question_list'),
  path('question/<int:pk>/', views.question_detail, name='question_detail'),
  path('ask/', views.ask_question, name='ask_question'),
]