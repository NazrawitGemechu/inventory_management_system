from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("products", views.products, name="products"),
    path("products/<slug>", views.product_detail, name="product_detail"),
    path("suppliers", views.suppliers, name="suppliers"),
    path("suppliers/<slug>",views.supplier_detail, name="supplier_detail")
]