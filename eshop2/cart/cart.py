from decimal import Decimal
from django.conf import settings
from products.models import Product
from common.services import filter_objects


class Cart(object):
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        """" Enumerates of elements in cart, gets Products from db,
            convert price to Decimal, adds total price to each element """
        product_ids = self.cart.keys()
        products = filter_objects(
            objects=Product.objects,
            id__in=product_ids
        )

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price'] * item['quantity'])
            yield item

    def __len__(self) -> int:
        """"counts all items in the cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def add_or_update(self, product, quantity=1) -> None:
        self.cart[str(product.id)] = {
            'quantity': quantity,
            'price': str(product.price)
        }
        self.save()

    def save(self) -> None:
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product_id) -> None:
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self) -> int:
        """counts price of all products in cart"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self) -> None:
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
