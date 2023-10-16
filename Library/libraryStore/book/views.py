from django.shortcuts import render
from django.core.paginator import Paginator 
from main.views import order_paginate
from .models import *

def category_related_books(request, cat):
    books = Books.objects.filter(sub_category__category__slug=cat)
    books = order_paginate(books,request)
    context = {"books" : books}
    return render(request, 'book/books.html', context)

def subcategory_related_books(request,cat,sub):   
    books = Books.objects.filter(sub_category__slug=sub)                        
    books = order_paginate(books,request)
    context = {"books" : books}
    return render(request, 'book/books.html', context)

  

