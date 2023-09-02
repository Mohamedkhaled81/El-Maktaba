from django.db import models
from django.utils.text import slugify


class BaseClass(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True,default=None)
    class Meta:
        abstract = True
    

    def save(self,*arges,**kwargs):
        self.slug = slugify(self.title)
        super().save(*arges,**kwargs)

    def __str__(self) -> str:
        return self.title


class Books(BaseClass):
    sub_category = models.ForeignKey('SubCategory',on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    image = models.ImageField(blank=True,default=None)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.SmallIntegerField()
    selled_quantity = models.SmallIntegerField()
    description = models.TextField()


    class Meta:
        db_table = 'Books'

class SubCategory(BaseClass):
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    class Meta:
        db_table = 'SubCategory'

class Category(BaseClass):

    class Meta:
        db_table = 'Category'

