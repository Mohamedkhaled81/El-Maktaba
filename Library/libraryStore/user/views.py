from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from main.views import home
# Create your views here.


def register(request):
    if 'search' in request.GET:
       return home(request)
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    return render(request, 'user/register.html', {'form': form})


class Login(LoginView):
    template_name = "user/login.html"
