from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product, Supplier, Sale, SoldProduct
from .forms import ProductForm,SupplierForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
# Create your views here.

class ProductListView(ListView):
    template_name= "inventory/products.html"
    model = Product
    context_object_name = "products"
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("product_name")
        return data
    
class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/add-product.html"
    success_url = "products"
    
def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    if product.quantity < product.threshold or product.quantity == product.threshold:
        above_threshold = product.quantity
        stock=False
    else:
        above_threshold=product.quantity - product.threshold
        stock=True
    return render(request,"inventory/product-detail.html",{
        "product":product,
        "threshold": above_threshold,
        "stock":stock
    })
    
class AddSupplierView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "inventory/add-supplier.html"
    success_url = "suppliers"
    
class SupplierListView(ListView):
    template_name = "inventory/suppliers.html"
    model = Supplier
    context_object_name = "suppliers"
    def get_queryset(self):
        base_query= super().get_queryset()
        data = base_query.order_by("supplier_name")
        return data
    
class SupplierDetailView(DetailView):
    template_name = "inventory/supplier-detail.html"
    model = Supplier