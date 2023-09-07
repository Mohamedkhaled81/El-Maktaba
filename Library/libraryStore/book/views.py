from django.shortcuts import render
from .models import Books

def showAllSubBooks(request, cat):
    books = Books.objects.filter(sub_category__category__title=cat)
    print(books)
    print(Books.objects.all())
    context = {"books" : books}
    return render(request, 'book/books.html', context)

def showSpecificSubBooks(request, sub):
    books = Books.objects.select_related(sub_category=sub)
    context = {"books" : books}
    return render(request, 'book/books.html', context)
