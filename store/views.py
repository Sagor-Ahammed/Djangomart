from django.shortcuts import get_object_or_404, render

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