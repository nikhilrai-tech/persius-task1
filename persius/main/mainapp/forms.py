from django import forms
from .models import Image, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'location']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email']