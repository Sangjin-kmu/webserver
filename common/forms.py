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
            'title': forms.TextInput(attrs={'class': 'border p-2 rounded w-full'}),
            'author': forms.TextInput(attrs={'class': 'border p-2 rounded w-full'}),
            'description': forms.Textarea(attrs={'class': 'border p-2 rounded w-full', 'rows': 4}),
            'published_date': forms.DateInput(attrs={'type': 'date', 'class': 'border p-2 rounded'}),
            'isbn': forms.TextInput(attrs={'class': 'border p-2 rounded w-full'}),
            'category': forms.TextInput(attrs={'class': 'border p-2 rounded w-full'}),
        }
