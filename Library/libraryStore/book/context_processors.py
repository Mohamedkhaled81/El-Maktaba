from .models import *

def show_all_categories(request):
    categories = Category.objects.prefetch_related('subset').all()
    context = {"categories" : categories}
    return context