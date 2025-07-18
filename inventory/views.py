from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product, Supplier, Sale, SoldProduct
from .forms import ProductForm,SupplierForm
from django.views import View
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
    
class AddProductView(View):
    def get(self,request):
        form = ProductForm()
        return render(request,"inventory/add-product.html",{
            "form":form
        })
    def post(self,request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("products")
        return render(request,"inventory/add-product.html",{
            "form":form
        })
    
def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    if product.quantity < product.threshold or product.quantity == product.threshold:
        above_threshold = product.quantity
    else:
        above_threshold=product.quantity - product.threshold
    return render(request,"inventory/product-detail.html",{
        "product":product,
        "threshold": above_threshold
    })
    
class AddSupplierView(View):
    def get(self, request):
        form = SupplierForm()
        return render(request, "inventory/add-supplier.html",{
            "form": form
        })
    def post(self,request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("suppliers")
        return render(request,"inventory/add-supplier.html",{
            "form":form
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