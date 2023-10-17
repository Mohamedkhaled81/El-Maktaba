from django.urls import path, include
from .views import *
from django.conf import settings


urlpatterns = [
    path('home/', home, name='Home-Page'),
    path('about', about, name='About-Page'),
    path('contact-us', ContactUs, name='ContactUs-Page'),
] 
