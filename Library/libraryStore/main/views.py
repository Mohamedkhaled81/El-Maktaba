from django.shortcuts import render
from book.models import Books
# Create your views here.
def home(request):
    books = Books.objects.all() 
    return render(request, 'main/home.html', {'books' : books})

def about(request):
    return render(request, 'main/about.html')

def ContactUs(request):
    return render(request, 'main/contact.html')
