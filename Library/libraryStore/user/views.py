from django.shortcuts import render, HttpResponse
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'user/register.html', {'form': form})
