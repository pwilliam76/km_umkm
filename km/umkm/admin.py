from django.contrib import admin
from umkm.models import *

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
	list_display = ['title', 'type_for', 'creator']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'parent']

class TagAdmin(admin.ModelAdmin):
	list_display = ['tag_title','description']

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['post_title', 'status', 'post_category']
	exclude = ['post_type']

admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)