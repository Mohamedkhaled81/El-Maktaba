from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='Home-Page'),
    path('about/', views.about, name='About-Page')
]