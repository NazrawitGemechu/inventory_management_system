from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("products", views.products, name="products-page"),
    path("products/<slug>", views.product_detail, name="product-detail"),
    path("suppliers", views.suppliers, name="suppliers-page"),
    path("suppliers<slug>",views.supplier_detail, name="supplier-detail")
]