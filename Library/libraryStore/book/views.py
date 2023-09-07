from django.shortcuts import render
from django.db.models import Q

from .models import *

def show_all(request, cat):
    books = Books.objects.filter(sub_category__category__slug=cat)
    context = {"books" : books}
    return render(request, 'book/books.html', context)

def show_sub(request, cat, sub):
    books = Books.objects.filter(Q(sub_category__category__slug=cat) &  Q(sub_category__slug=sub))
    print(books)
    context = {"books" : books}
    return render(request, 'book/books.html', context)
