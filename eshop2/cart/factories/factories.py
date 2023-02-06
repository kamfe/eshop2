import factory
from products.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = 'product'
    description = 'la-la-la'
    price = 300
    units_in_stock = 1000
    on_sale = True
