from django.contrib.sessions.backends.db import SessionStore
from django.test import TestCase, RequestFactory
from .factories.factories import ProductFactory
from cart.cart import Cart


class CartTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        session = SessionStore()
        session['cart'] = {}
        self.request.session = session

        self.cart = Cart(self.request)

    def test_add_product_in_cart(self):
        self.cart.add_or_update(ProductFactory(), quantity=5)
        self.cart.add_or_update(ProductFactory(name='other product'), quantity=100)
        self.cart.add_or_update(ProductFactory(name='another product'))

        self.assertEqual(len(self.cart), 3)

    def test_update_product(self):
        first_product = ProductFactory()
        self.cart.add_or_update(first_product, quantity=5)
        self.cart.add_or_update(first_product, quantity=10)

        self.assertEqual(len(self.cart), 1)

        cart = self.request.session['cart']
        self.assertEqual(cart[str(first_product.id)]['quantity'], 10)

    def test_cannot_add_the_same_product_twice(self):
        same_product = ProductFactory()
        self.cart.add_or_update(same_product, quantity=5)
        self.cart.add_or_update(same_product, quantity=5)

        self.assertEqual(len(self.cart), 1)

    def test_remove(self):
        product = ProductFactory()
        self.cart.add_or_update(product, quantity=5)
        self.cart.remove(product.id)

        self.assertEqual(len(self.cart), 0)

    def test_get_total_price(self):
        self.cart.add_or_update(ProductFactory(price=1), quantity=5)
        self.cart.add_or_update(ProductFactory(name='other product', price=5), quantity=10)

        self.assertEqual(self.cart.get_total_price(), 55)

    def test_clear(self):
        self.cart.add_or_update(ProductFactory())
        self.cart.clear()

        self.assertNotIn('cart', self.request.session.keys())

    def test_iter(self):
        first_product = ProductFactory(price=10)
        self.cart.add_or_update(first_product, quantity=5)

        second_product = ProductFactory(name='second product', price=100)
        self.cart.add_or_update(second_product, quantity=1)

        for i in self.cart:
            self.assertIn('product', i.keys())
            self.assertIn('price', i.keys())
            self.assertIn('total_price', i.keys())

        cart = self.request.session['cart']

        self.assertEqual(cart[str(first_product.id)]['product'], first_product)
        self.assertEqual(cart[str(first_product.id)]['price'], first_product.price)

        self.assertEqual(cart[str(second_product.id)]['product'], second_product)
        self.assertEqual(cart[str(second_product.id)]['price'], second_product.price)

    def test_get_product_ids_list(self):
        first_product = ProductFactory()
        self.cart.add_or_update(first_product, quantity=5)
        second_product = ProductFactory(name='second product')
        self.cart.add_or_update(second_product, quantity=1)

        self.assertEqual(self.cart.get_product_ids_list(), [int(first_product.id), int(second_product.id)])
