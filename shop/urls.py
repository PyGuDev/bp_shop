from django.urls import path
from .views import MainView, SingleProductView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('product/<int:pk>/', SingleProductView.as_view(), name='product')
]