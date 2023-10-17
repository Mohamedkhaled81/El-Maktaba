from django.shortcuts import render, redirect
from django.core.paginator import Paginator 
from book.models import Book
# Create your views here.

def home(request):
    books = Book.objects.all()
    books = search(books, request)
    books = order_paginate(books,request)
    return render(request, 'book/books.html', {'books' : books})

def order_paginate(queryset,request):
    order = request.GET.get('orderby')
    if order:
        queryset = queryset.order_by(order)  
    paginator = Paginator(queryset,8) 
    page_num = request.GET.get('page')
    queryset=paginator.get_page(page_num)
    return queryset

def search(queryset, request):
    if 'search' in request.GET:
        search = request.GET['search']
        exact = queryset.filter(title__iexact=search)
        if exact.exists():
            queryset = exact
        else:
            queryset = queryset.filter(title__icontains=search)
    return queryset



def about(request):
    if 'search' in request.GET:
       return home(request)
    return render(request, 'main/about.html')

def ContactUs(request):
    if 'search' in request.GET:
        return home(request)
    return render(request, 'main/contact.html')
