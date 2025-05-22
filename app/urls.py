from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:product_id>", views.products_details, name="product_details"),
    
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", views.cart_add, name="cart_add"),
    path("cart/remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("cart/update/<int:product_id>/", views.cart_update, name="cart_update"),
    path('registration/', views.registration_page, name='registration_page'),
]

