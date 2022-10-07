from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from carts.views import _cart_id
from carts.models import CartItem
from .models import Product,Variation
from category.models import Category

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q



def store(request,category_slug=None):
    categories =None
    products =None
    
    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True)
        product_count = products.count()
    else:

        products = Product.objects.all().filter(is_available=True)
        # paginator = Paginator(products,6)
        # page = request.GET.get('page')
        # paged_products = paginator.get_page(page)
        product_count = products.count()
        
    
    context={
        'products':products,
        
        'product_count':product_count,
    }
    return render(request,'store/store.html',context)


def product_details(request,category_slug,product_slug):
 
    try:
       
        variation_color = Variation.objects.filter(variation_category = 'color')
        variation_battery = Variation.objects.filter(variation_category = 'battery')
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart         = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e
    variations=Variation.objects.filter(product_id=single_product.id)
    context={
        'single_product':single_product,
        'in_cart':in_cart,
        'variation_color':variation_color,
        'variation_battery':variation_battery,
        'variations':variations,
        
    }
    return render(request,'store/product_details.html',context)


def search(request):
    if 'keyword' in request.GET:
        keyword =request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)| Q(product_name__icontains=keyword))
            product_count = products.count()
        context={
            'products':products,
            'product_count':product_count,

        }

    return render(request,'store/store.html',context)