from django.urls import path
from . import views 

urlpatterns = [
    path('<str:cat>', views.show_all, name='Cat-Page'),
    path('<str:cat>/<str:sub>', views.show_sub, name='sub&Cat-Page')
]