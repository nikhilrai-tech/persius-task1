from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm, CommentForm,CustomUserChangeForm
from .models import Image, Comment
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if(user.is_superuser):
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/profile/")
        return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploader = request.user
            image.save()
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def home(request):
    images = Image.objects.all()
    comments = Comment.objects.all()
    return render(request, 'home.html', {'images': images, 'comments': comments})

def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    comments = image.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return redirect("/", image_id=image_id)
    else:
        form = CommentForm()
    
    return render(request, 'image_detail.html', {'image': image, 'comments': comments, 'form': form})

@login_required
def update_profile(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('/profile/')
        else:
            form = CustomUserChangeForm(instance=user)
        return render(request, "updateprofile.html", {"form": form})
    else:
        return HttpResponseRedirect("/login/")

