from django.urls import path
from products.views import MainPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
]
