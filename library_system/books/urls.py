
from django.urls import path
from .views import unavailable_books

urlpatterns = [
    path('unavailable/', unavailable_books, name='unavailable_books'),
]