from django.urls import path
from . import views 

urlpatterns = [
    path('<str:cat>', views.show_all_books, name='Cat-Page'),
    path('<str:cat>/<str:sub>', views.show_related_books, name='sub&Cat-Page')
]