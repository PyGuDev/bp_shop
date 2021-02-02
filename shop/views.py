from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Products, CategoryProduct, ImagesForProduct


class MainView(ListView):
    model = Products
    template_name = 'shop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['category'] = CategoryProduct.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('s')
        if query:
            # сортировка по категория
            queryset = queryset.filter(category=query)
            print(queryset)
        return queryset


class SingleProductView(DetailView):
    model = Products
    template_name = 'shop/product.html'

