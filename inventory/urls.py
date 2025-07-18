from django.urls import path
from . import views
urlpatterns = [
    path("addproduct",views.AddProductView.as_view(),name = "add-product"),
    path("products", views.ProductListView.as_view(), name="products"),
    path("products/<slug>", views.product_detail, name="product_detail"),
    path("addsupplier",views.AddSupplierView.as_view(),name="add-supplier"),
    path("suppliers", views.SupplierListView.as_view(), name="suppliers"),
    path("suppliers/<slug>",views.supplier_detail, name="supplier_detail")
    
]