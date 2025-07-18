from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product, Supplier, Sale, SoldProduct
from .forms import ProductForm,SupplierForm
from django.views import View
from django.views.generic import ListView, DetailView
# Create your views here.
class ProductListView(ListView):
    template_name= "inventory/products.html"
    model = Product
    context_object_name = "products"
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("product_name")
        return data
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
        stock=False
    else:
        above_threshold=product.quantity - product.threshold
        stock=True
    return render(request,"inventory/product-detail.html",{
        "product":product,
        "threshold": above_threshold,
        "stock":stock
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