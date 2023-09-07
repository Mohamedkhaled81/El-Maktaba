from django.shortcuts import render
from django.db.models import Q

from .models import *

def show_all_books(request, cat):
    books = Books.objects.all()
    context = {"books" : books}
    return render(request, 'book/books.html', context)

# for showing the related books for each sub category
def show_related_books(request, cat, sub):
    print(request.path)
    #books = Books.objects.filter(Q(sub_category__category__slug=cat) &  Q(sub_category__slug=sub))
    # books = Books.objects.select_related('sub_category').filter(sub_category__slug=sub)     
    books = Books.objects.filter(sub_category__slug=sub)         
    print(books)                   
    print('dasd')                 
    context = {"books" : books}
    return render(request, 'book/books.html', context)
