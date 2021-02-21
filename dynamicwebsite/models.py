from django.db import models
from django.contrib import admin

# Create your models here.
class Products(models.Model):
    itemname = models.CharField(max_length=100)
    itemprice = models.FloatField()
    photo = models.ImageField(upload_to='productsphotos/')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('itemname','itemprice')

class People(models.Model):
    membername = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='peoplephotos/')

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('membername','designation')