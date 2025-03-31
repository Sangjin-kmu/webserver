from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Post
from django.http import HttpResponse


def user_login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
      login(request, user)
      return redirect('/write/')
  return render(request, 'login.html')


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

def csrf_attack(request):
  return render(request, 'attack.html')