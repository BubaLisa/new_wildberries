from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:product_id>", views.products_details, name="product_details"),
    
    path("basket/", views.basket_detail, name="basket_detail"),
    path("basket/add/<int:product_id>/", views.basket_add, name="basket_add"),
    path("basket/remove/<int:product_id>/", views.basket_remove, name="basket_remove"),
    ]

