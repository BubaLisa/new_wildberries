from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart  
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

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

def cart_clear(request):
    cart = Cart(request)
    cart.clear()  # Вызываем метод очистки
    return redirect('cart_detail')  # Перенаправляем обратно в корзину

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'app/cart_detail.html', {'cart': cart})

def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    action = request.POST.get('action')  # 'increment' или 'decrement'

    if action == 'increment':
        cart.add(product=product, quantity=1)  # увеличиваем на 1
    elif action == 'decrement':
        current_quantity = cart.cart.get(str(product.id), {}).get('quantity', 0)
        if current_quantity > 1:
            cart.add(product=product, quantity=-1)  # уменьшаем на 1
        else:
            cart.remove(product)  # если 1, то удаляем

    return redirect('cart_detail')

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
            user = form.save()
            login(request, user)
            return redirect('index') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/registration_page.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app/index.html')  # или куда хочешь после логина
    else:
        form = AuthenticationForm()
    return render(request, 'app/login_page.html', {'form': form})