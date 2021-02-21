from django.contrib import admin
from .models import Products,ProductsAdmin
from .models import People,PeopleAdmin

# Register your models here.

admin.site.register(Products,ProductsAdmin)
admin.site.register(People,PeopleAdmin)