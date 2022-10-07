from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mkhome.urls')),
    path('adminapp/',include('adminapp.urls')),
    path('category/',include('category.urls')),
    path('store/',include('store.urls')),
    path('carts/',include('carts.urls')),
    path('orders/',include('orders.urls')),
    path('lensoadmin/',include('lensoadmin.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
