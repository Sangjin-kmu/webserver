from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Rating, Book

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': '질문을 입력하세요...',
                'class': 'w-full p-2 border rounded resize-none'
            }),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        widgets = {
            'score': forms.Select(attrs={
                'class': 'border p-2 rounded',
            }, choices=[(i, f"{i}점") for i in range(1, 6)])
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'image', 'description', 'published_date', 'isbn', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': '제목 입력',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded bg-white'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': '저자 입력',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded bg-white'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-700 border border-gray-300 rounded bg-white file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:bg-blue-600 file:text-white hover:file:bg-blue-700'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': '책 설명 입력',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded bg-white',
                'rows': 4
            }),
            'published_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded bg-white'
            }),
            'isbn': forms.TextInput(attrs={
                'placeholder': 'ISBN 입력',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded bg-white'
            }),
            'category': forms.TextInput(attrs={
                'placeholder': '카테고리 입력',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded bg-white'
            }),
        }
