from django.contrib import admin
from .models import Category, Post
# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display= ('title','description','url')
    search_fields= ('title',)
class AdminPost(admin.ModelAdmin):
    list_display= ('title',)
    search_fields= ('title',)
    list_filter= ('cat',)
    list_per_page=10

    class Media:
        js=("https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js",'js/script.js',)


admin.site.register(Category,AdminCategory)
admin.site.register(Post,AdminPost)
