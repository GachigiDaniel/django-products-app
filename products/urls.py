from django.urls import path
from products import views  # Use absolute import instead of relative

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('', views.product_list, name='product_list'),
]