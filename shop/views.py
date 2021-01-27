from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Products, CategoryProduct, ImagesForProduct


class MainView(ListView):
    model = Products
    template_name = 'shop/index.html'


class SingleProductView(DetailView):
    model = Products
    template_name = 'shop/product.html'

