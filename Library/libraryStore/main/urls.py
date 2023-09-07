from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='Home-Page'),
    path('books/', include('book.urls')),
    path('about/', views.about, name='About-Page'),
    path('ContactUs/', views.ContactUs, name='ContactUs-Page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
