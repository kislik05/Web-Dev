from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:pk>/cars/', views.CarsInCategory.as_view(), name='cars-in-category'),
]