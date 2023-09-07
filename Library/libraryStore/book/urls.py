from django.urls import path
from . import views 

urlpatterns = [
    path('<str:cat>/', views.showAllSubBooks, name='Cat-Page'),
    path('<str:sub>/', views.showSpecificSubBooks, name='sub&Cat-Page')
]