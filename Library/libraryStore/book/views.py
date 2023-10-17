from django.shortcuts import render
from django.core.paginator import Paginator 
from main.views import order_paginate, search
from .models import *

def category_related_books(request, cat):
    books = Book.objects.filter(sub_category__category__slug=cat)
    books = search(books, request)
    books = order_paginate(books,request)
    context = {"books" : books}
    return render(request, 'book/books.html', context)

def subcategory_related_books(request,cat,sub):   
    books = Book.objects.filter(sub_category__slug=sub)
    books = search(books, request)                    
    books = order_paginate(books,request)
    context = {"books" : books}
    return render(request, 'book/books.html', context)

def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    print(book)
    context = {
        'book' : book
    }
    return render(request, 'book/details.html', context)
