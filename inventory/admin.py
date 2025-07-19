from django.contrib import admin
from .models import Product, Supplier,SoldProduct,Sale


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_name",)}
class SupplierAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("supplier_name",)}


admin.site.register(Product,ProductAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(SoldProduct)
admin.site.register(Sale)