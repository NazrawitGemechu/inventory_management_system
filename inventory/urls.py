from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("addproduct",views.AddProductView.as_view(),name = "add-product"),
    path("products", views.products, name="products"),
    path("products/<slug>", views.product_detail, name="product_detail"),
    path("addsupplier",views.AddSupplierView.as_view(),name="add-supplier"),
    path("suppliers", views.suppliers, name="suppliers"),
    path("suppliers/<slug>",views.supplier_detail, name="supplier_detail")
    
]