from django.urls import path
from . import views
urlpatterns = [
    path("addproduct",views.AddProductView.as_view(),name = "add-product"),
    path("products", views.ProductListView.as_view(), name="products"),
    path("products/<slug>", views.product_detail, name="product_detail"),
    path("updateproduct/<slug>",views.UpdateProductView.as_view(),name="update-product"),
    path("deleteproduct/<slug>",views.DeleteProduct.as_view(),name="delete-product"),
    path("addsupplier",views.AddSupplierView.as_view(),name="add-supplier"),
    path("suppliers", views.SupplierListView.as_view(), name="suppliers"),
    path("suppliers/<slug>",views.SupplierDetailView.as_view(), name="supplier_detail"),
    path("updatesupplier/<slug>",views.UpdateSupplierView.as_view(), name="update-supplier"),
    path("deletesupplier/<slug>",views.DeleteSupplier.as_view(),name="delete-supplier")
    
]