from django.shortcuts import render, redirect
from .forms import ContactUsForm

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def ContactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ContactUs-Page')
    form = ContactUsForm()
    return render(request, 'main/contact.html', {'form' : form})
