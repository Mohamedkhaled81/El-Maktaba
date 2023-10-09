from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mssg = models.TextField(verbose_name='Message')