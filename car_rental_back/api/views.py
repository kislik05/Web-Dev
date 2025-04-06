from django.shortcuts import render
from rest_framework import generics
from .models import Car, CarCategory
from .serializers import CarSerializer, CarCategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer

class CarsInCategory(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        category_id = self.kwargs['id']
        return Car.objects.filter(category_id=category_id)