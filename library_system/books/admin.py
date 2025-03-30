from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'copies_available', 'is_available')
    search_fields = ('title', 'author')