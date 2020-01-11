"""makjumia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings  #new 
from django.conf.urls.static import static #new
from django.urls import path
from home.views import *

urlpatterns = [
    path('',indexview, name='home'),
    path('categories/',categoriesView,name='category'),
    path('catnavigation/',categoriesNavView,name='categorynav'),
    path('categories/<int:category_id>/',categoriesView,name='category'),
    path('categories/subcategory/<int:subcategory_id>',subcategoriesView,name='subcategory'),
    path('checkouts/',checkOutView,name='checkout'),
    path('products/<int:product_id>/',productPageView,name='product'),
    path('products/',productsPageView,name='product'),
    path('contacts/',contactView,name='contact'),
    path('orders/',shoppingCartView,name='order'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)