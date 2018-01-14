from django.contrib import admin
from .models import Category, Tag, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (['name'])

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (['name',])

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'created_date')
