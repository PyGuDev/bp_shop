from django.shortcuts import render
from django.views.generic import ListView

from .models import Products, CategoryProduct, ImagesForProduct


class MainView(ListView):
    model = Products
    template_name = 'shop/index.html'


