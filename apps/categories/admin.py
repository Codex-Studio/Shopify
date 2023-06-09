from django.contrib import admin

from apps.categories.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
    list_per_page = 20
    prepopulated_fields = {'slug' : ('title', )}