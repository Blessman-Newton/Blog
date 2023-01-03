from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.http import HttpResponseRedirect
from .models import Post
from .form import AddPost
from django.contrib import messages
# Create your views here.

def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts':posts})


def post(request, pk):
	blog = Post.objects.get(id=pk)
	return render(request, 'post.html', {'blog':blog})



def register(request):
    if request.method == "POST":
        fname = request.POST['fierstname']
        lname = request.POST['lastname']
        username = request['username']
        mname = request.POST['middlename']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(request,email=email).exists():
                message.info("Email already exist")
                redirect('login')
            elif User.objects.filter(request,username=username).exists():
                message.info("User already exist")
                redirect('login')
            else:
                user = User.objects.create_user(fname=firstname, lname=lastname, mname=middlename,
                                                username=username, email=email, password1=password1)
                user.save()
                redirect('login')
        else:
            message.info("Password do not match")
            redirect('register')
    return render(request,'register.html')



def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password1']
        
        user = authenticate(request, email=email, password1=password1)
        if user is not None:
            login(request,user)
            redirect('index')
        else:
            message.info('Invaild Credentials')
            redirect('login')
    return render(request, 'login.html', {'email':email, 'password':password1})



def add_post(request):
    post_form = AddPost()
    if request.method == 'POST':
        add_new_post = AddPost(request.POST)
        if add_new_post.is_vaild():
            add_new_post.save()
    return render(request, 'add_post.html', {'post_form':post_form, 'add_new_post':add_new_post})



def update(request, pk):
    call_post = Post.objects.get(id=pk)
    update_post = AddPost(instance= call_post)
    if request.mehtod == 'POST':
        update_post = AddPost(instance=call_post)
        if update_post.is_valid():
            update_post.save()
            return redirect('index')
    return render(request, 'update.html', {'call_post':call_post, 'update_post':update_post})



def delete(request, pk):
    if request.method == 'POST':
        delete_post = Post.objects.get(id=pk)
        delete_post.delete()
        return HttpResponseRedirect(reversed('add_post'))

    

def logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reserve('login'))
    

def search(request):
    if request.method == 'POST':
        search_qurey = request.POST['search_query']
        if search_qurey:
            search_post = Post.objects.filter(headline__icontains=search_qurey)
            return render(request, 'search.html', {'search_qurey':search_qurey, 'search_post':search_post})
        
    return render(request, 'search.html')