from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Supplier, Sale, SoldProduct
# Create your views here.
def index(request):
    products = Product.objects.all().order_by("product_name")[:10]
    return render(request,"inventory/index.html",{
        "products": products
    })

def products(request):
    products = Product.objects.all().order_by("product_name")
    return render(request, "inventory/products.html",{
        "products":products
    })
def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,"inventory/product-detail.html",{
        "product":product
    })
def suppliers(request):
    suppliers = Supplier.objects.all().order_by("supplier_name")
    return render(request,"inventory/suppliers.html",{
        "suppliers":suppliers
    })
def supplier_detail(request,slug):
    supplier = Supplier.objects.get(slug=slug)
    return render(request,"inventory/supplier-detail.html",{
        "supplier":supplier
    })