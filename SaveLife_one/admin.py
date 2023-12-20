from django.contrib import admin
from .models import Blog,Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','text_intro','slug','date_added')
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body','email','date_added')
    
    
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)