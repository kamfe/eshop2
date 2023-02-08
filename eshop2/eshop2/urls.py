from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include(('products.urls', 'products'), namespace='products')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
]
if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
    )
