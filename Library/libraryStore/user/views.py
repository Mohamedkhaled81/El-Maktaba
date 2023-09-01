from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("tmmam")
    return render(request, 'user/register.html', {'form': form})


class Login(LoginView):
    template_name = "user/login.html"


class Logout(LogoutView):
    template_name = "user/logout.html"