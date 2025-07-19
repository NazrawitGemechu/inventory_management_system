from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product, Supplier, Sale, SoldProduct
from .forms import ProductForm,SupplierForm,SoldProductForm
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView,DeleteView
from django.views.generic.edit import CreateView
from dateutil.relativedelta import relativedelta
from datetime import date
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
    
class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/add-product.html"
    success_url = "../products"
    
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

class DeleteProduct(DeleteView):
    model = Product
    template_name = "inventory/delete-product.html"
    success_url ="../products"
    
class SoldProductView(View):
    def get(self,request):
        form = SoldProductForm()
        return render(request, "inventory/sale-product.html",{
            "form":form
        })
    def post(self,request):
        form = SoldProductForm(request.POST)
        if form.is_valid():
            sale = Sale.objects.create()
            sold_product =form.save(commit = False)
            sold_product.sale =sale
            sold_product.save()
            product= sold_product.product
            quantity = sold_product.quantity
            new_quantity = product.quantity - quantity
            product.quantity = new_quantity
            product.save()
            return HttpResponseRedirect("sells")
        return render(request,"inventory/sell-product.html",{
            "form":form
        })
  
def check_exp(request):
    products = Product.objects.all()
    product_list =[]
    for product in products:
        exp = product.expiry_date
        today = date.today()
        six_month_later = today + relativedelta(months=6)
        if exp <= six_month_later:
            product_list.append(product)
    return render(request,"inventory/exp-warning.html",{
        "products":product_list
    })
            
class SellListView(ListView):
    model = SoldProduct
    template_name = "inventory/sells.html"
    context_object_name = "sells"
   
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
class UpdateSupplierView(UpdateView):
    model = Supplier
    form_class= SupplierForm
    template_name = "inventory/add-supplier.html" 
    success_url = "../suppliers"
class SupplierDetailView(DetailView):
    template_name = "inventory/supplier-detail.html"
    model = Supplier
class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = "inventory/delete-supplier.html"
    success_url = "../suppliers"