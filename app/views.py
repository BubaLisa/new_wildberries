from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .basket import Basket
from django.core.paginator import Paginator

def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 7)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    pagination_range = get_pagination(page_obj.number, paginator.num_pages)

    context = {"page_obj": page_obj,
            "pagination_range": pagination_range,
            }
    return render(request, "app/index.html", context)

def products_details(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = []
    categories.append(product.category)
    cur_category = product.category
    while cur_category.parent:
        categories.append(cur_category.parent)
        cur_category = cur_category.parent
    categories.reverse()
    context = {"product": product, "categories": categories}
    return render(request, "app/product_details.html", context)    

def get_pagination(current_page, total_pages, delta=2):
    left = current_page - delta
    right = current_page + delta + 1
    range_pages = []

    for i in range(1, total_pages + 1):
        if i == 1 or i == total_pages or (left <= i < right):
            range_pages.append(i)
        elif range_pages[-1] != '...':
            range_pages.append('...')
    return range_pages      

def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.add(product=product, quantity=1)
    return redirect('basket_detail')

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.remove(product)
    return redirect('basket_detail')

def basket_detail(request):
    basket = Basket(request)
    return render(request, 'app/basket_detail.html', {'basket': basket})
