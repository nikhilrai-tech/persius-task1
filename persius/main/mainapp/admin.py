from django.contrib import admin
from .models import Comment,Image

@admin.register(Image)
class commentadmin(admin.ModelAdmin):
    list_display=["id","image","location","uploader"]

@admin.register(Comment)
class commentadmin(admin.ModelAdmin):
    list_display=["id","image","content"]