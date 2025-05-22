from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart  
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm

def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 7)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    pagination_range = get_pagination(page_obj.number, paginator.num_pages)

    context = {
        "page_obj": page_obj,
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

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'app/cart_detail.html', {'cart': cart})

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    action = request.POST.get("action")

    if action == "increment":
        cart.add(product=product, quantity=1, update_quantity=False)
    elif action == "decrement":
        if cart.cart[str(product_id)]["quantity"] > 1:
            cart.add(product=product, quantity=-1, update_quantity=False)
        else:
            cart.remove(product)

    return redirect("cart_detail")

def registration_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/registration_page.html', {'form': form})
