from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<slug:slug>/", views.products_details, name="product_details"),
    
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", views.cart_add, name="cart_add"),
    path("cart/remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("cart/update/<int:product_id>/", views.cart_update, name="cart_update"),
    path('cart/clear/', views.cart_clear, name='cart_clear'),

    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),  # добавляем вход
    path("logout/", views.logout_view, name="logout"),
]

