from django.views.generic import TemplateView, ListView
from products.models import Product, Category
from common.services import all_objects, filter_objects, available_products


class HomePageView(TemplateView):
    template_name = 'products/index.html'


class ProductsPageView(ListView):
    model = Product
    paginate_by = 9
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = all_objects(Category.objects)
        return context

    def get_queryset(self):
        return available_products(Product.objects)


class ProductsOfSelectedCategoryPageView(ProductsPageView):
    def get_queryset(self):
        return filter_objects(
            objects=available_products(Product.objects),
            category=self.kwargs['category_id']
        )
