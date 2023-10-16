from django.shortcuts import render
from django.core.paginator import Paginator 
from book.models import Books
# Create your views here.

def home(request):
    books = Books.objects.all()
    books = order_paginate(books,request)
    return render(request, 'book/books.html', {'books' : books})


def order_paginate(queryset,request):
    order = request.GET.get('orderby')
    if order:
        queryset = queryset.order_by(order)  
    paginator = Paginator(queryset,5) 
    page_num = request.GET.get('page')
    queryset=paginator.get_page(page_num)
    return queryset


def about(request):
    return render(request, 'main/about.html')

def ContactUs(request):
    return render(request, 'main/contact.html')
