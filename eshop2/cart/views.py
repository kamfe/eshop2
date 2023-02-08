from django.shortcuts import HttpResponseRedirect, get_object_or_404
from cart.cart import Cart
from products.models import Product


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add_or_update(product)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
