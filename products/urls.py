from django.urls import path
from . import views

urlpatterns = [
    # Produits
    path("", views.product_list, name="product_list"),
    path("<int:id>/", views.product_detail, name="product_detail"),

    # Catégories
    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:id>/", views.category_detail, name="category_detail"),
    path("cart/", views.cart, name="cart"),
]