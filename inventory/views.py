from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Supplier, Sale, SoldProduct
# Create your views here.
def index(request):
    products = Product.objects.all().order_by("product_name")[:10]
    names = ', '.join([p.product_name for p in products])
    return HttpResponse(f"products: {names}")
def products(request):
    products = Product.objects.all().order_by("product_name")
    names = ', '.join([p.product_name for p in products]) 
    return HttpResponse(f"Products: {names}")
def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,"inventory/product-detail.html",{
        "product":product
    })
def suppliers(request):
    suppliers = Supplier.objects.all().order_by("supplier_name")
    names = ", ".join({s.supplier_name for s in suppliers})
    return HttpResponse(f"suppliers name: {names}")
def supplier_detail(request,slug):
    supplier = Supplier.objects.get(slug=slug)
    return render(request,"inventory/supplier-detail.html",{
        "supplier":supplier
    })