from django.urls import path
from products.views import (HomePageView,
                            ProductsPageView,
                            ProductsOfSelectedCategoryPageView)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path(
        'products/<str:category_id>',
        ProductsOfSelectedCategoryPageView.as_view(),
        name='products_of_selected_category'
    ),
]
