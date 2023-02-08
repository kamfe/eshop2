from django.urls import path
from cart.views import cart_add, cart_remove


urlpatterns = [
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('remove/<int:product_id>', cart_remove, name='cart_remove'),
]
