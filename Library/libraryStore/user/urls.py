from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


from . import views


urlpatterns = [
    path('register', views.register, name='Register'),
    path('login', views.Login.as_view(), name='Login'),
    path('logout', LogoutView.as_view(
        next_page=reverse_lazy('Home-Page')), name='Logout'),
]
