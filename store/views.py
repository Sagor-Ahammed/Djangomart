
from aifc import Error
from django.shortcuts import get_object_or_404, render
from requests import request 

# Create your views here.
from . models import Product,Category

def store(request,category_slug=None):
    categories=Category.objects.all()
    products=None
    if category_slug!= None:
        category=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=category,is_available=True)
        product_count=products.count()
    else:    
        products = Product.objects.all().filter(is_available=True)
        product_count=products.count()
    return render (request,'store/store.html',{'products':products, 'p_count':product_count,'categories':categories})


def product_details(request,category_slug,product_slug):
    try:    
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception  as e:
        raise e
    context={
        'single_product':single_product
    }
    return render (request,'store/product_details.html',context)
    