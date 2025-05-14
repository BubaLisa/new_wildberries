from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "app/index.html", context)

def products_details(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = []
    categories.append(product.categories)
    cur_category
