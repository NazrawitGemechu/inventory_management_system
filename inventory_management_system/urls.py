"""
URL configuration for inventory_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('inventory/', include(('inventory.urls', 'inventory'), namespace='inventory')),
    path("", include("inventory.urls")),
    #path('admin/', admin.site.urls),
    #path('inventory/', include(('inventory.urls', 'inventory'), namespace='inventory')),
    #path('accounts/login/',views.login_view,name='login'),
    #path('accounts/logout/',views.logout_view,name='logout'),
    #path('accounts/register/',views.register_view,name='register')
    #path('inventory/', include("inventory.urls"))
]
