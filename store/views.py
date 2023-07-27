
from aifc import Error
from django.shortcuts import get_object_or_404, render
from requests import request 
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
from . models import Product,Category

def store(request,category_slug=None):
    categories=Category.objects.all()
    products=None
    if category_slug!= None:
        category=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=category,is_available=True)
        paginator=Paginator(products,1)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        product_count=products.count()
    else:    
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator=Paginator(products,3)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        product_count=products.count()
    context={
        'products':paged_products,
        'p_count':product_count
    }    
    return render (request,'store/store.html',context)


def product_details(request,category_slug,product_slug):
    try:    
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception  as e:
        raise e
    context={
        'single_product':single_product
    }
    return render (request,'store/product_details.html',context)
    
    
def search(request):
    if  'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            products=Product.objects.order_by('-create_date').filter (Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count=products.count()
    context={
        'products':products,
        'p_count':product_count
    }        
            
    return  render (request,'store/store.html',context)