from django.urls import path
from . import views 


urlpatterns = [
    path('<str:cat>', views.category_related_books, name='Cat-Page'),
    path('<str:cat>/<str:sub>', views.subcategory_related_books, name='sub&Cat-Page'),   
]
