from django.shortcuts import render
from .models import Book
from django.http import JsonResponse, HttpResponse


def unavailable_books(request):
    book = Book.objects.all()

    books_list = [x for x in book]

    s = ""
    for b in books_list:
        s += b
    # return JsonResponse(book, safe=False)
    return HttpResponse('<h1>Hello<h1/>' + s)