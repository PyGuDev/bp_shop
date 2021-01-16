from django.contrib import admin
from .models import ImagesForProduct, Products, CategoryProduct


admin.site.register(Products)
admin.site.register(ImagesForProduct)
admin.site.register(CategoryProduct)
