from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:cat>', views.category_related_books, name='Cat-Page'),
    path('<str:cat>/<str:sub>', views.subcategory_related_books, name='sub&Cat-Page'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)