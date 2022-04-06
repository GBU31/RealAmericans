from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def signup(request):
    ""

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'msg':'Error'})
    return render(request, 'login.html')



@login_required(login_url='/login')
def home(request):
    all_post = post.objects.all()
    pic = profilePic.objects.all()
    all_ver = ver.objects.all()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            form2 = form.save(commit=False)
            form2.user = request.user
            form2.save()

    return render(request, 'home.html', {'post_form':form,'all_post':all_post, 'User':str(request.user), 'pic':pic,'all_ver':all_ver})


@login_required(login_url='/login')
def profile(request):
    all_post = post.objects.filter(user=str(request.user))
    all_ver = ver.objects.all()
    pic = profilePic.objects.filter(user=str(request.user))
    return render(request, 'profile.html', {'all_post':all_post,'User':str(request.user), 'pic':pic,'all_ver':all_ver})