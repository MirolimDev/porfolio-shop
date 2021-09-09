from django.db import models
from django.db.models import fields
from ckeditor.fields import RichTextField
# from translations.models import Translatable

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="static_files/images/category")
    slug = models.CharField(max_length=50)
    parent_id = models.ForeignKey('Category', models.CASCADE, 'category_to_category_pk', blank=True, null=True)

    def __str__(self):
        return self.name    

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to="static_files/images/product")
    slug = models.CharField(max_length=50)
    category_id = models.ForeignKey('Category', on_delete = models.CASCADE)
    old_price = models.IntegerField()
    price = models.IntegerField()

    # class TranlatableMeta:
    #     fields = ['name', 'description']

    def __str__(self):
        return self.name


class Slider(models.Model):
    top_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    buttom_title = models.CharField(max_length=150)
    buttom_html = models.TextField()
    clas = models.CharField(max_length=150)
    sort = models.IntegerField()


