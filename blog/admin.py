from django.contrib import admin

# Register your models here.
from .models import (Category, Post)
from .forms import (CategoryForm, PostForm)

class CategoryAdmin(admin.ModelAdmin):
	form = CategoryForm
	list_display = ['name', 'creation',]
	list_display_links = ['name']
	search_fields = ['name']


class PostAdmin(admin.ModelAdmin):
	form = PostForm
	list_display = ['title', 'author', 'creation']
	list_filter = ['categories', 'author', 'creation']
	search_fields = ['title']

	def save_model(self, request, obj, form, change):
		form.instance.author = request.user
		form.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
