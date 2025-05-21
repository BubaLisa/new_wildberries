from decimal import Decimal
from django.conf import settings
from .models import Product

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket')
        if not basket:
            basket = self.session['basket'] = {}
        self.basket = basket

    def add(self, product, quantity = 1):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] += quantity
        else:
            self.basket[product_id] = {
                'quantity': quantity,
                'price': str(product.price)
            }
        self.save()

    def save(self):
        self.session['basket'] = self.basket
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def iter(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product
        for item in basket.values():
            item['total_price'] = float(item['price']) * item['quantity']
            yield item

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.basket.values())