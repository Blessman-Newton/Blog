from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts':posts})


def post(request, pk):
	blog = Post.objects.get(id=pk)
	return render(request, 'post.html', {'blog':blog})



def register(request):
	return render(request, 'register.html')



def login(request):
	return render(request, 'login.html')




def add_post(request):
	return render(request, 'add_post.html')



def update(request):
	return render(request, 'update.html')



def delete(request):
	return render(request, 'delete.html')



def search(request):
	return render(request, 'search.html')