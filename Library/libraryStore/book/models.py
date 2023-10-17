from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from PIL import Image


class BaseClass(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True,default=None)
    class Meta:
        abstract = True
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self) -> str:
        return self.title


class Book(BaseClass):
    sub_category = models.ForeignKey('SubCategory',on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    image = models.ImageField(blank=True,default=None,upload_to='images/')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.SmallIntegerField()
    selled_quantity = models.SmallIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField("Date", default=timezone.now)

    class Meta:
        db_table = 'Books'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            resize = (300,300)
            img.thumbnail(resize)
            img.save(self.image.path) 
    

class SubCategory(BaseClass):
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='subset')

    class Meta:
        db_table = 'SubCategory'

class Category(BaseClass):
    
    class Meta:
        db_table = 'Category'

