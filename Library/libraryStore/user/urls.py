from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register),
    path('login', views.Login.as_view()),
    path('logout', views.Logout.as_view()),
]
