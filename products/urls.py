from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:id>/", views.product_detail, name="product_detail"),

    # PANIER
    path("cart/", views.cart, name="cart"),
    path("cart/add/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:id>/", views.remove_from_cart, name="remove_from_cart"),
]