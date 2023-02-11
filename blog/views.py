from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .form import AddPost
from django.contrib import messages
# Create your views here.



def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts':posts})

@login_required(login_url='/login/')
def post(request, pk):
	blog = Post.objects.get(id=pk)
	return render(request, 'post.html', {'blog':blog})



def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                message.info("Email already exist")
                return redirect('login')
            elif User.objects.filter(username=username).exists():
                messagse.info(request, "User already exist")
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info("Password do not match")
            return redirect('register')
    return render(request,'register.html')



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        
        else:
            messages.info(request, "Invaild Credentials")
            return redirect('register')
        
    return render(request, 'login.html')


@login_required(login_url='/login/')
def add_post(request):
    post_form = AddPost()
    if request.method == 'POST':
        post_form = AddPost(request.POST)
        if post_form.is_valid():
            post_form.save()
    return render(request, 'add_post.html', {'post_form':post_form})


@login_required(login_url='/login/')
def update(request, pk):
    call_post = Post.objects.get(id=pk)
    update_post = AddPost(instance= call_post)
    if request.mehtod == 'POST':
        update_post = AddPost(instance=call_post)
        if update_post.is_valid():
            update_post.save()
            return redirect('index')
    return render(request, 'update.html', {'call_post':call_post, 'update_post':update_post})


@login_required(login_url='/login/')
def delete(request, pk):
    if request.method == 'POST':
        delete_post = Post.objects.get(id=pk)
        delete_post.delete()
        return HttpResponseRedirect(reversed('add_post'))

    

def logout(request):
	if request.method == 'POST':
		logout(request)
		return HttpResponseRedirect(reverse('login'))
    
@login_required(login_url='/login/')
def search(request):
    if request.method == 'POST':
        search_qurey = request.POST['search_query']
        if search_qurey:
            search_post = Post.objects.filter(headline__icontains=search_qurey)
            return render(request, 'search.html', {'search_qurey':search_qurey, 'search_post':search_post})
        
    return render(request, 'search.html')