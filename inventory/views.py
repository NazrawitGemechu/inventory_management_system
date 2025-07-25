from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product, Supplier, Sale, SoldProduct
from .forms import ProductForm,SupplierForm,SoldProductForm
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView,DeleteView
from django.views.generic.edit import CreateView
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from datetime import date
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.
def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

class ProductListView(LoginRequiredMixin,ListView):
    template_name= "inventory/products.html"
    model = Product
    context_object_name = "products"
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("product_name")
        return data
    
class AddProductView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/add-product.html"
    success_url = "products"
    
class UpdateProductView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/update-product.html"
    success_url = "../products"
    
@login_required
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

class DeleteProduct(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = "inventory/delete-product.html"
    success_url ="../products"
    def dispatch(self, request, *args, **kwargs):
        if not is_admin(request.user):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    
class SoldProductView(LoginRequiredMixin,View):
    def get(self,request):
        form = SoldProductForm()
        return render(request, "inventory/sell-product.html",{
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
            return HttpResponseRedirect("dashboard")
        return render(request,"inventory/sell-product.html",{
            "form":form
        })
   
class MostSelledView(LoginRequiredMixin,ListView):
    model = SoldProduct
    template_name = "inventory/most-selled.html"
    context_object_name = "products"
    def get_queryset(self):
        products = Product.objects.annotate(total_sold=Sum('soldproduct__quantity')).order_by('-total_sold')
        return products
def dashboard(request):
    cos_products = Product.objects.filter(category='cosmetic')
    cos_count =cos_products.count()
    med_products = Product.objects.filter(category='medicine')
    med_count=med_products.count()
    suppliers = Supplier.objects.all()
    sup_count = suppliers.count()
    products = Product.objects.all()
    low_count = 0
    product_count = 0
    exp_count = 0
    product_list =[]
    for product in products:
        product_count +=1
        if product.quantity < product.threshold or product.quantity == product.threshold:
            in_stock = False
            low_count+=1
        else:
            in_stock = True
    for product in products:

        exp = product.expiry_date
        today = date.today()
        six_month_later = today + relativedelta(months=6)
        if exp <= six_month_later:
            product_list.append(product)
            exp_count += 1
    sold = SoldProduct.objects.order_by('-sale__sold_at')[:5]

    
    return render(request,"inventory/dashboard.html",{
        "med_count":med_count,
        "cos_count":cos_count,
        "sup_count":sup_count,
        "in_stock": in_stock,
        "low_count": low_count,
        "total":product_count,
        "exp_count":exp_count,
        "product_list":product_list,
        "sold":sold
    })
class AddSupplierView(LoginRequiredMixin,CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "inventory/add-supplier.html"
    success_url = "suppliers"
    
class SupplierListView(LoginRequiredMixin,ListView):
    template_name = "inventory/suppliers.html"
    model = Supplier
    context_object_name = "suppliers"
    def get_queryset(self):
        base_query= super().get_queryset()
        data = base_query.order_by("supplier_name")
        return data
class UpdateSupplierView(LoginRequiredMixin,UpdateView):
    model = Supplier
    form_class= SupplierForm
    template_name = "inventory/update-supplier.html" 
    success_url = "../suppliers"
class SupplierDetailView(LoginRequiredMixin,DetailView):
    template_name = "inventory/supplier-detail.html"
    model = Supplier
class DeleteSupplier(LoginRequiredMixin,DeleteView):
    model = Supplier
    template_name = "inventory/delete-supplier.html"
    success_url = "../suppliers"
    def dispatch(self, request, *args, **kwargs):
        if not is_admin(request.user):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)